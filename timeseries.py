import twitter
import csv
from matplotlib import pyplot as plt
api=twitter.Api(consumer_key ="TqYo5eyOnfS90TE0lRlCv9N1e", consumer_secret = "odVkD7cF1yGsB9AYo6Q8vHh65Ls2TdkUm6HH9V0P0y2SFhlCCs", access_token_key= "297344628-qIBS3Cu1nHy4IVtcgHZvh3ys1BpfP7H0yIuFCE32", access_token_secret = "6AZDGMVxrJ2TRbINxIGmjMGfssXw5GWbR0DyeY3VegTir", tweet_mode="extended")
user = api.GetUserTimeline(screen_name="NIH", count=200, include_rts=False)
earliest = min(user, key=lambda x: x.id).id
while True:
    newtweets = api.GetUserTimeline(screen_name="NIH", max_id=earliest, count=200)
    n_early = min(newtweets, key=lambda x: x.id).id
    if newtweets and n_early != earliest:
        earliest = n_early
        user += newtweets
    else:
        break
# user2 = api.GetUserTimeline(screen_name="CDCGlobal", count=200, include_rts=False)
# user3 = api.GetUserTimeline(screen_name="WHO", count=200, include_rts=False)
# user4 = api.GetUserTimeline(screen_name="WebMD", count=200, include_rts=False)
with open("C:/Users/deban/Classes/fall 2020/CS 490A/finalproj/timestamp.csv", 'w',newline="\n", encoding='utf8') as output:
    writer = csv.writer(output, delimiter=",")
    
    writer.writerows([tweet.created_at] for tweet in user)
    # writer.writerows([tweet.created_at] for tweet in user2)
    # writer.writerows([tweet.created_at] for tweet in user3)
    # writer.writerows([tweet.created_at] for tweet in user4)
list = []
count = {} 
with open("C:/Users/deban/Classes/fall 2020/CS 490A/finalproj/timestamp.csv", "r") as f:
    reader = csv.reader(f, delimiter=" ")
    for i, line in enumerate(reader):
        list.append(line[1])
for i in list: 
    count[i] = count.get(i, 0) + 1
print(count)

#plotting
plt.plot(*zip(*count.items()))
plt.xlabel("Months")
plt.ylabel("Frequency")
plt.show() 
       