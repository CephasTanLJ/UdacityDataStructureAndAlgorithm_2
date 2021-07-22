class Group(object):
    def __init__(self, name):
        self.name = name
        self.groups = list()
        self.users = list()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        return f'Name: {self.name} Group: {self.groups} Users: {self.users}'

def is_user_in_group(user, group):
    if user in group.get_users():
        return True
    else:
        for g in group.get_groups():
            if is_user_in_group(user, g):
                return True
    return False

def test():
    parent = Group('parent')
    child = Group('child')
    sub_child = Group('sub_child')

    sub_child_user = 'sub_child_user'
    sub_child.add_user(sub_child_user)
    parent.add_user('me')

    child.add_group(sub_child)
    parent.add_group(child)

    assert is_user_in_group('sub_child_user', parent) == True, 'Test 1'
    assert is_user_in_group('sub_child_user', child) == True, 'Test 2'
    assert is_user_in_group('sub_child_user', sub_child) == True, 'Test 3'
    assert is_user_in_group('child_user', parent) == False, 'Test 4'
    assert is_user_in_group('sub_child_user', parent) == True, 'Test 5'

    child2 = Group('child2')
    child2.add_user('anotherChild_user')
    parent.add_group(child2)
    is_user_in_group('anotherChild_user', parent)
    assert is_user_in_group('anotherChild_user', parent) == True, 'Test 6'
    assert is_user_in_group('anotherChild_user', sub_child) == False, 'Test 7'



if __name__=='__main__':
    test()
    print('Done')