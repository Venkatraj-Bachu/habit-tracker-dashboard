import datetime

# Import your custom modules for creating a user, graph, posting, updating, and deleting pixels
from create_user import CreateUser
from create_graph import CreateGraph
from post_pixel import PostPixel
from update_pixel import UpdatePixel
from delete_pixel import DeletePixel

# Constants for the user's information
USERNAME = "venkatraj"
TOKEN = "sjhfsafhlakfjsafoi"

# Base URL for the Pixela API
pixela_endpoint = "https://pixe.la/v1/users"

# Get the current date in "YYYYMMDD" format
today = datetime.datetime.now().strftime("%Y%m%d")

# Creating a user
pixel_user = CreateUser(USERNAME, TOKEN)
# pixel_user.create_user()  # Uncomment this line to create a user

# Creating a new graph in the users profile
new_graph_name = 'New Graph'
new_graph_id = 'graph2'
new_graph_data_type = 'float'
new_graph_unit_measure = 'minutes'

new_graph = CreateGraph(username=USERNAME, password=TOKEN,
                        graph_id=new_graph_id, graph_name=new_graph_name,
                        data_type=new_graph_data_type, unit_measure=new_graph_unit_measure)
# new_graph.create_graph() # Uncomment this line to create a new graph

# Posting an entry to a graph

new_post_quantity = '2.5'
new_post_date = today
new_post = PostPixel(username=USERNAME, password=TOKEN, quantity=new_post_quantity, date=today)
# new_post.post_pixel(graph_id=new_graph_id) # Uncomment this line to post a pixel

# Updating an existing Pixel

update_quantity = '1.83'
update_date = today
update_pixel = UpdatePixel(username=USERNAME, password=TOKEN, graph_id=new_graph_id)
# update_pixel.update_pixel(date=update_date, new_quantity=update_quantity)  # Uncomment this line to update a pixel


# Deleting an existing Pixel
graph_to_delete = 'graph2'
entry_to_delete = today
delete_pixel = DeletePixel(username=USERNAME, password=TOKEN)
# delete_pixel.delete_pixel(graph_id=graph_to_delete, date=entry_to_delete)  # Uncomment this line to delete a pixel
