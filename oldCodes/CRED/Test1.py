import requests

emailAddressSet = {''}

filePAth = ''

PostIds = 


for curRequest in GetAllPost.json():
    curPostId = curRequest['id']
    commentsURL = 'https://jsonplaceholder.typicode.com/posts/' + str(curPostId) + '/comments'
    comments = requests.get(commentsURL)
    for comment in comments.json():
        emailAddressSet.add(comment['email'])


print(emailAddressSet[1:])

