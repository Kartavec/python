from functools import reduce
from settings import INSTALLED_APPS


def get_server_actions():
    modules = reduce(
        lambda value, item: value + [__import__(f'{item}.actions')],
        INSTALLED_APPS,
        [])
    actions = reduce(
        lambda value, item: value + [getattr(item, 'action', [])],
        modules,[])
    return reduce(
        lambda value, item: value + getattr(item, 'actionnames', []),
        actions,
        [])

def resolve(action_name, actions=None):
    action_list = actions or get_server_actions()
    actions_mapping = {
        action.get('action'): action.get('controller')
        for action in action_list}
    return actions_mapping.get(action_name)