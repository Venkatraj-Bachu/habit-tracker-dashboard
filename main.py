import datetime

from create_user import CreateUser
from create_graph import CreateGraph
from post_pixel import PostPixel
from update_pixel import UpdatePixel
from delete_pixel import DeletePixel


USERNAME = "venkatraj"
TOKEN = "sjhfsafhlakfjsafoi"

pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.datetime.now().strftime("%Y%m%d")

# Creating a user
pixel_user = CreateUser(USERNAME, TOKEN)
# pixel_user.create_user()

# Creating a new graph in the users profile

new_graph_name = 'New Graph'
new_graph_id = 'graph2'
new_graph_data_type = 'float'
new_graph_unit_measure = 'minutes'

new_graph = CreateGraph(username=USERNAME, password=TOKEN,
                        graph_id=new_graph_id, graph_name=new_graph_name,
                        data_type=new_graph_data_type, unit_measure=new_graph_unit_measure)
new_graph.create_graph()

# Posting an entry to a graph

new_post_quantity = '2.5'
new_post_date = today
new_post = PostPixel(username=USERNAME, password=TOKEN, quantity=new_post_quantity, date=today)
# new_post.post_pixel(graph_id=new_graph_id)

# Updating an existing Pixel

update_quantity = '1.83'
update_date = today
update_pixel = UpdatePixel(username=USERNAME, password=TOKEN, graph_id=new_graph_id)
# update_pixel.update_pixel(date=update_date, new_quantity=update_quantity)

# Deleting an existing Pixel
graph_to_delete = 'graph2'
entry_to_delete = today
delete_pixel = DeletePixel(username=USERNAME, password=TOKEN)
delete_pixel.delete_pixel(graph_id=graph_to_delete, date=entry_to_delete)
