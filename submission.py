import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from IPython.display import display
import tensorflow as tf
from sklearn.utils import resample

df_ratings = pd.read_csv('ml-latest/ratings.csv')
df_movies = pd.read_csv('ml-latest/movies.csv')
df_tags = pd.read_csv('ml-latest/tags.csv')
df_tags.dropna(inplace=True)

df_ratings_new = pd.DataFrame()
target_count = 10000

for rating, group in df_ratings.groupby('rating'):
    if len(group) > target_count:
        ratings_new = resample(group, replace=False, n_samples=target_count, random_state=42)
    else:
        ratings_new = group
    df_ratings_new = pd.concat([df_ratings_new, ratings_new])
df_ratings = df_ratings_new.sort_values(by='userId').reset_index(drop=True)
df_movies = df_movies[df_movies['movieId'].isin(df_ratings['movieId'])]
df_movies = df_movies.sort_values(by='movieId').reset_index(drop=True)
df_tags = df_tags[df_tags['movieId'].isin(df_ratings['movieId'])]
df_tags = df_tags.sort_values(by='userId').reset_index(drop=True)

df_tags = df_tags.groupby('movieId')['tag'].agg(lambda x: ' '.join(x)).reset_index()
df_movies['genres'] = df_movies['genres'].apply(lambda x: x.replace("|"," "))
df_movies_similarity = pd.merge(df_movies,df_tags,how='left',on='movieId')
df_movies_similarity.fillna(' ',inplace=True)
df_movies_similarity['tags'] = df_movies_similarity['genres'] + " " + df_movies_similarity['tag']
df_movies_similarity.drop(columns=['genres','tag'],inplace=True)
df_ratings_movie= pd.merge(df_ratings,df_movies,how='left',on='movieId')
df_ratings_movie.drop(columns=['timestamp'],axis=1,inplace=True)
df_ratings_movie['genres'] = df_ratings_movie['genres'].apply(lambda x: np.nan if x == '(no genres listed)' else x)
df_ratings_movie.dropna(inplace=True)
df_ratings_movie.reset_index()
df_ratings_movie['genres'] = df_ratings_movie['genres'].str.split(' ')
df_genres = df_ratings_movie['genres'].apply(lambda x: pd.Series([1] * len(x), index=x)).fillna(0).astype(int)
df_ratings_encode= pd.concat([df_ratings_movie, df_genres], axis=1)
df_ratings_encode.drop(columns=['genres'],inplace=True)

df_user = df_ratings_encode.copy()
df_user.drop(columns=['movieId','title'],inplace=True)
for i in range(2, 21):
    genre_column = df_user.columns[i]
    df_user[genre_column] = df_user.apply(lambda row: row['rating'] if row[genre_column] == 1 else np.nan,axis=1)
genre_columns = df_user.columns[2:]
df_user_avg = df_user.groupby('userId')[genre_columns].mean().reset_index()
df_user_avg.fillna(0,inplace=True)
df_user = pd.merge(df_user,df_user_avg,how='left',on='userId')
df_user.drop(columns=df_user.columns[1:21],inplace=True)
df_user.columns = ['userId'] + genre_columns.tolist()
df_item = df_ratings_encode.copy()
df_item.drop(columns=['userId','rating','title'],inplace=True)
rating = df_ratings_encode['rating'].values

scaler_user = StandardScaler()
scaler_item = StandardScaler()

scaler_user.fit(df_user[genre_columns])
scaler_item.fit(df_item[genre_columns])

df_user[genre_columns] = scaler_user.transform(df_user[genre_columns])
df_item[genre_columns] = scaler_item.transform(df_item[genre_columns])

scaler = MinMaxScaler((-1,1))
scaler.fit(rating.reshape(-1,1))
rating = scaler.transform(rating.reshape(-1,1))

user_train, user_test, item_train, item_test, rating_train, rating_test = train_test_split(df_user[genre_columns], df_item[genre_columns], rating.flatten(), test_size=0.2, random_state=42)
user_test, user_val, item_test, item_val, rating_test, rating_val = train_test_split(user_test, item_test, rating_test, test_size=0.5, random_state=42)

cv = CountVectorizer(max_features = 2000, lowercase=True)
vectors = cv.fit_transform(df_movies_similarity['tags']).toarray()
cosine_sim = cosine_similarity(vectors)
def get_recommendation_movie(title):
    index = df_movies[df_movies['title'] == title].index[0]
    similarity_score = cosine_sim[index] 
    similarity_place = sorted(enumerate(similarity_score),key=lambda x: x[1],reverse=True)[1:11]
    similarity_list = []    
    for i in similarity_place:
        similarity_list.append(df_movies.iloc[i[0],:3].tolist() + [i[1]])
    similarity_df = pd.DataFrame(similarity_list, columns=['movieId','title', 'genres','similarity_score'])
    return similarity_df
test_movie = 'Toy Story (1995)'
top_10_recommendation = get_recommendation_movie(test_movie)
test_movie = df_movies[df_movies['title'] == test_movie]

features = 19

user_model = tf.keras.Sequential([
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(64, activation='linear')
])

item_model = tf.keras.Sequential([
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(64, activation='linear')
])

input_user = tf.keras.Input(shape=(features,))
vector_user = user_model(input_user)
vector_user = tf.linalg.l2_normalize(vector_user, axis=1)

input_item = tf.keras.Input(shape=(features,))
vector_item = item_model(input_item)
vector_item = tf.linalg.l2_normalize(vector_item, axis=1)

output = tf.keras.layers.Dot(axes=1)([vector_user, vector_item])

model = tf.keras.Model(inputs=[input_user, input_item], outputs=output)

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])

history = model.fit([user_train, item_train], rating_train, epochs=20, verbose=2, batch_size=256, validation_data=([user_val, item_val], rating_val))

new_user_id = 500000
new_adventure = 4
new_animation = 5
new_children = 4
new_comedy = 3
new_fantasy = 4
new_romance = 1
new_action = 1
new_crime = 1
new_thriller = 1
new_mystery = 1
new_horror = 1
new_drama = 1
new_war = 1
new_western = 1
new_scifi = 1
new_musical = 1
new_filmnoir = 1
new_imax = 1
new_documentary = 1
new_user = pd.DataFrame([[new_user_id, new_adventure, new_animation, new_children, new_comedy, new_fantasy, new_romance, new_action, new_crime, new_thriller, new_mystery, new_horror, new_drama, new_war, new_western, new_scifi, new_musical, new_filmnoir, new_imax, new_documentary]], columns=['userId', 'Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy', 'Romance', 'Action', 'Crime', 'Thriller', 'Mystery', 'Horror', 'Drama', 'War', 'Western', 'Sci-Fi', 'Musical', 'Film-Noir', 'IMAX', 'Documentary'])
new_user[genre_columns] = scaler_user.transform(new_user[genre_columns])
new_user = np.tile(new_user[genre_columns], (df_item.shape[0], 1))
predictions = model.predict([new_user, df_item[genre_columns]])
predictions = scaler.inverse_transform(predictions)
sorted_predictions = np.argsort(predictions, axis=0)[::-1].flatten()
sorted_item = df_ratings.index.to_numpy()[sorted_predictions].flatten()
dic_predictions = {
    'userId': np.full((df_item.shape[0],), new_user_id),
    'index': df_ratings_movie.iloc[sorted_item].index,
    'predictions': predictions[sorted_predictions].flatten()
} 
df_predictions = pd.DataFrame(dic_predictions)
df_predictions.set_index('index', inplace=True)
df_predictions = pd.merge(df_predictions, df_ratings_movie, how='left', left_index=True, right_index=True).reset_index(drop=True)
df_predictions.drop_duplicates(subset=['movieId'], inplace=True)
df_predictions.drop(columns=['userId_y', 'rating'], inplace=True)
df_predictions.rename(columns={'userId_x': 'userId'}, inplace=True)
df_predictions.reset_index(drop=True,inplace=True)
def calculate_precision(recommended_movies, relevant_movies):
    recommended_movies = set(recommended_movies)
    relevant_movies = set(relevant_movies)
    return len(recommended_movies.intersection(relevant_movies)) / len(recommended_movies)
relevant_id = top_10_recommendation['movieId'].tolist()
relevant_movies = top_10_recommendation[top_10_recommendation['movieId'].isin(relevant_id)]
precision = calculate_precision(top_10_recommendation['movieId'], relevant_movies['movieId'])
print(f'Precision: {precision:.2f}') 
val_mse, val_loss = model.evaluate([user_val, item_val], rating_val, verbose=2)
