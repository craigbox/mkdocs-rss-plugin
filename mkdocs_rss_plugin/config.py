#! python3  # noqa: E265

# ############################################################################
# ########## Libraries #############
# ##################################


# 3rd party
from mkdocs.config import config_options
from mkdocs.config.base import Config


# ############################################################################
# ########## Classes ###############
# ##################################
class RssPluginConfig(Config):
    """Configuration for RSS plugin for Mkdocs."""

    abstract_chars_count = config_options.Type(int, default=160)
    abstract_delimiter = config_options.Type(str, default="<!-- more -->")
    categories = config_options.Type(list, default=None)
    comments_path = config_options.Type(str, default=None)
    date_from_meta = config_options.Type(dict, default=None)
    enabled = config_options.Type(bool, default=True)
    feed_ttl = config_options.Type(int, default=1440)
    image = config_options.Type(str, default=None)
    length = config_options.Type(int, default=20)
    match_path = config_options.Type(str, default=".*")
    pretty_print = config_options.Type(bool, default=False)
    url_parameters = config_options.Type(dict, default=None)
