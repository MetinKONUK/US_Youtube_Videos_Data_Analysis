import pandas as pd
df = pd.read_csv("USvideos.csv")

#1. Read first 5 lines
print(df.head(n = 5))

#2. Delete columns
#thumbnail_link,video_id,trending_date,publish_time,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed
df.drop(labels = ["thumbnail_link", "video_id" ,"trending_date" ,"publish_time", "thumbnail_link", "comments_disabled", "ratings_disabled" ,"video_error_or_removed"],
        inplace = True,
        axis = 1)
print(df.head(2))

#3. Find Rows, Columns Counts
print("Rows : {}\nColumns : {}".format(df.shape[0], df.shape[1]))

#4. Find the average value of likes and dislikes
print(df["likes"].mean(), df["dislikes"].mean(), sep = "\t")

#5. Find the most viewed videos title
mv = df["views"].max()
print("Most viewed video title:", df.loc[df["views"] == mv]["title"].iloc[0], sep="\t")

#6. Find the least viewed videos title
lv = df["views"].min()
print("Least viewed video title:", df.loc[df["views"] == lv]["title"].iloc[0], sep = "\t")

#7. Find the average comment counts based on categories
print(df.groupby(by = "category_id")["comment_count"].mean())

#8. Find count of videos on each category
print(df.groupby(by = "category_id", sort = True)["title"].count())

#9. Create a new column indicating each videos title length
df["title_length"] = df["title"].apply(len)
print(df)

#10. Create a new column indicating tag counts for each video
df["tag_counts"] = df["tags"].apply(lambda s: s.count("|")+1)
print(df)

#11. Sort videos by like count, descending
def lidiratio(likes, dislikes):   
    likesl, dislikesl, ratios = [], [], []
    for key, value in list(likes.iteritems()):
        likesl.append(value)
    for key, value in list(dislikes.iteritems()):
        dislikesl.append(value)
    for l, d in zip(likesl, dislikesl):
        if not (l+d):
            ratios.append(0)
        else:
            ratios.append(l / (d+l))
    return ratios
#print(lidiratio(df["likes"], df["dislikes"]))
#Interpreting above line migth struggle your computer
df["ld_ratio"] = lidiratio(df["likes"], df["dislikes"])
df.sort_values("ld_ratio", ascending = False, inplace = True)
print(df)
    
    

    

