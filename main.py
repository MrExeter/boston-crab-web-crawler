import os

# Each website you crawl is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


def show_path(filename):
    try:
        user_paths = os.environ['HOME']
        data_directory = user_paths + '/DATA/New_Boston_Crawler/' + filename
        # print(data_directory)
        return data_directory
        
    except KeyError:
        user_paths = []


def make_full_path(filename):
    try:
        user_paths = os.environ['HOME']
        data_directory = user_paths + '/DATA/New_Boston_Crawler/' + filename
        # print(data_directory)
        return data_directory

    except KeyError:
        user_paths = []
        

create_project_dir(make_full_path('thenewboston'))