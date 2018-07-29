from surprise import SVD
from surprise import Dataset
from surprise import KNNWithMeans,accuracy
from surprise.model_selection import cross_validate,train_test_split

__all__ = ['show_top_five','show_equaly_film','get_all_users','get_all_films']
#Dictionaries we gonna use
dict_itens_by_id = dict()
dict_id_by_itens = dict()
watched = dict()
wasnt_watched = dict()


'''
Gettin all itens from the data base.
    Arranging into a dictonary adding key=id and value=item_name
'''
itens = open('../data/ml-100k/u.item',encoding="ISO-8859-1")
item_data = itens.read().split('\n')
for info in item_data:
    split = info.split('|')
    if(split != ['']):
        id_item = (split[0])
        film = (split[1])
        dict_itens_by_id[id_item]=[film]

        dict_id_by_itens[film]=id_item
itens.close()

'''
Getting films that user have been watched
     Arranging into a dictonary adding key=id and value=item_name 
'''
base = open('../data/ml-100k/u1.base',encoding="ISO-8859-1")
item_base = base.read().split('\n')
for usr_info in item_base:
    split = usr_info.split('\t')
    if(split != ['']):
        key = split[0]
        value = split[1]
        if(key in watched):
            watched[key].append(value)
        else:
            watched[key] = [value]
base.close()


'''
Getting films that user didnt watch
     Arranging into a dictonary adding key=id and value=item_name 
'''
films_list = set(dict_itens_by_id.keys())
for i in watched:
    films_list_user = set(watched[i])
    wasnt_watched[i] = films_list.difference(films_list_user)

'''
Training our data using KNN
'''
data = Dataset.load_builtin('ml-100k')

trainset,testset = train_test_split(data,test_size =.20)

algo_KNN = KNNWithMeans(k=4, sim_options={'name': 'cosine', 'user_based': True})

algo_KNN.fit(trainset)
predictions_knn = algo_KNN.test(testset)


def get_5_films(uid):
    '''
    using the trained model for predict our filme users,
        this function will return the top 5 films to the parse
        user id
        Args:
        --------
        uid: Id from User
        Return:
        -------
        top_5: The 5 films most recomendaded to the uid
    '''
    predict = []
    films_from_user = list(wasnt_watched[uid])

    for i in films_from_user:
        predict.append((i,algo_KNN.predict(uid=uid,iid=str(i)).est))
    predict = sorted(predict, key=lambda x: x[1],reverse = True)
    top_5 = predict[:5]
    return top_5

def show_top_five(uid):
    '''
    Show the top five films to the user
    Args:
    --------
        uid:Id from user
    Return:
    --------
        top_five: list that contains the 5 itens to the user
    '''
    top_five = tuple()
    first_five = get_5_films(uid)
    for w in first_five:
        print(dict_itens_by_id[w[0]],w[1])


def show_equaly_film(film_name):
    '''
        That function will return a film depending of 
            the entry film
        Args:
        --------
            film_name: a film name and his date
        Return:
        --------
            the name of the closest film
    '''
    film_raw_id = dict_id_by_itens[film_name]
    film_inner_id = algo_KNN.trainset.to_inner_iid(film_raw_id)
    print((dict_itens_by_id[str(film_inner_id)]))

def get_all_users():
	print(list(watched.keys()))

def get_all_films():
	print(list(dict_id_by_itens.keys()))

if __name__ == '__main__':
    #get_all_users()
    #get_all_films()
    #print('---------')
    show_top_five('360')
    print('---------')
    show_equaly_film('Toy Story (1995)')