class Comment:
    """The comment"""
    def __init__(self, pk=0, post_id=0, commenter_name="", comment=""):
        self.pk = pk
        self.post_pk = post_id
        self.commenter_name = commenter_name
        self.comment = comment

    def __repr__(self):

        return f"Comment(" \
               f"{self.pk}," \
               f" {self.post_pk}," \
               f" {self.commenter_name}," \
               f" {self.comment}" \
               f")"
