class Post:
    def __init__(self,
                 pk,
                 poster_name,
                 poster_avatar,
                 pic,
                 content,
                 views_count,
                 likes_count
                 ):
        self.pk = pk
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count

    def __repr__(self):
        return f"Post(" \
               f"{self.pk}," \
               f"{self.poster_name}, " \
               f"{self.poster_avatar}, " \
               f"{self.pic}, " \
               f"{self.content}, " \
               f"{self.views_count}, " \
               f"{self.likes_count}" \
               f")"
