############# TAGS #############
class Tag:
    """use to check attributes of things. stealth type characters, slaying abilities, etc."""
    def __init__(self, name, type_with_tag, context):
        self.name = name
        self.type_with_tag = type_with_tag
        self.context = context

    def check_context(self, target):
        """check the scope of a tag's use against a target to see if it applies"""
        if self.context[0] in target.type:
            if self.context[1] in target.tags:
                print("TRUE")
            else:
                print("FALSE")
        else:
            print("FALSE")