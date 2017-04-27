import os


# Each website you crawl is a separate project (folder)
def create_project_dir(directory):
    # Change simple project name to full directory name
    directory = make_full_path(directory)
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)
    return directory


def make_full_path(sub_dirname):
    try:
        user_paths = os.environ['HOME']
        full_path = user_paths + '/DATA/New_Boston_Crawler/' + sub_dirname
        return full_path

    except KeyError:
        user_paths = []


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data to an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# create_project_dir('thenewboston')