# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs  # noqa: E501

    OpenAPI spec version: v1.0 alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PostResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'activity_id': 'str',
        'actor': 'ActivityUser',
        'content': 'str',
        'created_at': 'int',
        'hashtags': 'list[str]',
        'id': 'str',
        'images': 'list[str]',
        'location': 'object',
        'matches': 'list[Match]',
        'own_reactions': 'dict(str, list[PostReactionResponse])',
        'reaction_counts': 'dict(str, Number)',
        'tags': 'list[ActivityUser]',
        'updated_at': 'int',
        'verb': 'str'
    }

    attribute_map = {
        'activity_id': 'activityId',
        'actor': 'actor',
        'content': 'content',
        'created_at': 'createdAt',
        'hashtags': 'hashtags',
        'id': 'id',
        'images': 'images',
        'location': 'location',
        'matches': 'matches',
        'own_reactions': 'ownReactions',
        'reaction_counts': 'reactionCounts',
        'tags': 'tags',
        'updated_at': 'updatedAt',
        'verb': 'verb'
    }

    def __init__(self, activity_id=None, actor=None, content=None, created_at=None, hashtags=None, id=None, images=None, location=None, matches=None, own_reactions=None, reaction_counts=None, tags=None, updated_at=None, verb=None):  # noqa: E501
        """PostResponse - a model defined in Swagger"""  # noqa: E501
        self._activity_id = None
        self._actor = None
        self._content = None
        self._created_at = None
        self._hashtags = None
        self._id = None
        self._images = None
        self._location = None
        self._matches = None
        self._own_reactions = None
        self._reaction_counts = None
        self._tags = None
        self._updated_at = None
        self._verb = None
        self.discriminator = None
        self.activity_id = activity_id
        self.actor = actor
        self.content = content
        self.created_at = created_at
        self.hashtags = hashtags
        self.id = id
        self.images = images
        self.location = location
        self.matches = matches
        self.own_reactions = own_reactions
        self.reaction_counts = reaction_counts
        self.tags = tags
        self.updated_at = updated_at
        self.verb = verb

    @property
    def activity_id(self):
        """Gets the activity_id of this PostResponse.  # noqa: E501


        :return: The activity_id of this PostResponse.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this PostResponse.


        :param activity_id: The activity_id of this PostResponse.  # noqa: E501
        :type: str
        """
        if activity_id is None:
            raise ValueError("Invalid value for `activity_id`, must not be `None`")  # noqa: E501

        self._activity_id = activity_id

    @property
    def actor(self):
        """Gets the actor of this PostResponse.  # noqa: E501


        :return: The actor of this PostResponse.  # noqa: E501
        :rtype: ActivityUser
        """
        return self._actor

    @actor.setter
    def actor(self, actor):
        """Sets the actor of this PostResponse.


        :param actor: The actor of this PostResponse.  # noqa: E501
        :type: ActivityUser
        """
        if actor is None:
            raise ValueError("Invalid value for `actor`, must not be `None`")  # noqa: E501

        self._actor = actor

    @property
    def content(self):
        """Gets the content of this PostResponse.  # noqa: E501


        :return: The content of this PostResponse.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PostResponse.


        :param content: The content of this PostResponse.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this PostResponse.  # noqa: E501


        :return: The created_at of this PostResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PostResponse.


        :param created_at: The created_at of this PostResponse.  # noqa: E501
        :type: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def hashtags(self):
        """Gets the hashtags of this PostResponse.  # noqa: E501


        :return: The hashtags of this PostResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._hashtags

    @hashtags.setter
    def hashtags(self, hashtags):
        """Sets the hashtags of this PostResponse.


        :param hashtags: The hashtags of this PostResponse.  # noqa: E501
        :type: list[str]
        """
        if hashtags is None:
            raise ValueError("Invalid value for `hashtags`, must not be `None`")  # noqa: E501

        self._hashtags = hashtags

    @property
    def id(self):
        """Gets the id of this PostResponse.  # noqa: E501


        :return: The id of this PostResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostResponse.


        :param id: The id of this PostResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def images(self):
        """Gets the images of this PostResponse.  # noqa: E501


        :return: The images of this PostResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this PostResponse.


        :param images: The images of this PostResponse.  # noqa: E501
        :type: list[str]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

    @property
    def location(self):
        """Gets the location of this PostResponse.  # noqa: E501


        :return: The location of this PostResponse.  # noqa: E501
        :rtype: object
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PostResponse.


        :param location: The location of this PostResponse.  # noqa: E501
        :type: object
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def matches(self):
        """Gets the matches of this PostResponse.  # noqa: E501


        :return: The matches of this PostResponse.  # noqa: E501
        :rtype: list[Match]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this PostResponse.


        :param matches: The matches of this PostResponse.  # noqa: E501
        :type: list[Match]
        """
        if matches is None:
            raise ValueError("Invalid value for `matches`, must not be `None`")  # noqa: E501

        self._matches = matches

    @property
    def own_reactions(self):
        """Gets the own_reactions of this PostResponse.  # noqa: E501


        :return: The own_reactions of this PostResponse.  # noqa: E501
        :rtype: dict(str, list[PostReactionResponse])
        """
        return self._own_reactions

    @own_reactions.setter
    def own_reactions(self, own_reactions):
        """Sets the own_reactions of this PostResponse.


        :param own_reactions: The own_reactions of this PostResponse.  # noqa: E501
        :type: dict(str, list[PostReactionResponse])
        """
        if own_reactions is None:
            raise ValueError("Invalid value for `own_reactions`, must not be `None`")  # noqa: E501

        self._own_reactions = own_reactions

    @property
    def reaction_counts(self):
        """Gets the reaction_counts of this PostResponse.  # noqa: E501


        :return: The reaction_counts of this PostResponse.  # noqa: E501
        :rtype: dict(str, Number)
        """
        return self._reaction_counts

    @reaction_counts.setter
    def reaction_counts(self, reaction_counts):
        """Sets the reaction_counts of this PostResponse.


        :param reaction_counts: The reaction_counts of this PostResponse.  # noqa: E501
        :type: dict(str, Number)
        """
        if reaction_counts is None:
            raise ValueError("Invalid value for `reaction_counts`, must not be `None`")  # noqa: E501

        self._reaction_counts = reaction_counts

    @property
    def tags(self):
        """Gets the tags of this PostResponse.  # noqa: E501


        :return: The tags of this PostResponse.  # noqa: E501
        :rtype: list[ActivityUser]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PostResponse.


        :param tags: The tags of this PostResponse.  # noqa: E501
        :type: list[ActivityUser]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def updated_at(self):
        """Gets the updated_at of this PostResponse.  # noqa: E501


        :return: The updated_at of this PostResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PostResponse.


        :param updated_at: The updated_at of this PostResponse.  # noqa: E501
        :type: int
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def verb(self):
        """Gets the verb of this PostResponse.  # noqa: E501


        :return: The verb of this PostResponse.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this PostResponse.


        :param verb: The verb of this PostResponse.  # noqa: E501
        :type: str
        """
        if verb is None:
            raise ValueError("Invalid value for `verb`, must not be `None`")  # noqa: E501
        allowed_values = ["MATCH", "POST"]  # noqa: E501
        if verb not in allowed_values:
            raise ValueError(
                "Invalid value for `verb` ({0}), must be one of {1}"  # noqa: E501
                .format(verb, allowed_values)
            )

        self._verb = verb

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PostResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
