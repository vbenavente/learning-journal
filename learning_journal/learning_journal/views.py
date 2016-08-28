from pyramid.view import view_config

ENTRIES = [
    {"title": "Vic Week 3 Day 2 Python", "creation_date": "Aug 23, 2016", "id": 1, "body": "Today we reviewed the heap data structure after doing some code review. Then we continued to learn how to implement Pyramid. I feel like we are rushing through this part a bit, the docs are good and can be followed well, but if I make a mistake while following along, I don't have time to catch back up I just have to sit back and watch. In lab we finished up our deque data structure and started planning our tests for heap. I am getting a bit behind on the learning journal. I was able to do step 1 in class while following along, but have not deployed my mockups. I plan on getting caught up with this assignment tomorrow. I was able to us bootstrap for the styling of my mockups so the learning journal has a much cleaner look."},
    {"title": "Vic Week 3 Day 1 Python", "creation_date": "Aug 22, 2016", "id": 2, "body": "Today we started with some code review of the HTTP server that was assigned last week and then we talked about the deque data structure. We got an introduction to Pyramid and it was good to run through the code during class, I found the class documentation to be relatively easy to follow for Pyramid. During lab time we pitched some project ideas and then got to work on our data structure assignment. We found that we had some bugs in code we wrote last week for doubly linked list and found it when trying to import those methods into our deque assignment. We are getting better at writing tests and got some good suggestions from Will on how to improve our testing. For the deployment of our learning journal, even though deploying to heroku went smoothly in Lecture, we ran into some bugs we are still dealing with when we tried to deploy our learning journal during lab time."},
    {"title": "Vic Week 2 Day 5 Python", "creation_date": "Aug 19, 2016", "id": 3, "body": "Today we started off with a 30 minute coding challenge. I find these the most stressful part of my day and Thursday night. It turned out not to be as bad as I was making it, but I definitely struggled with copy and paste into python. %paste is your friend. The white boarding was helpful as always. I realized I am still wanting to get straight into writing code as opposed to thinking about the real world solution. So I still need to change my mindset going into these. The rest of the day was productive. We all but finished up the doubly linked lists and got up to the 4th assignment for the http server. There is quite a bit to do over the weekend still."},
    {"title": "Vic Week 2 Day 4 Python", "creation_date": "Aug 18, 2016", "id": 4, "body": "Today in Lecture we did some code review to begin as usual and I got some good feedback on some code I wrote, ways to improve it and mistakes I had made. The data structure we talked about was the queue. Then we discussed properties and Concurrency. We also talked about using the threading and multiprocessing modules in Python. I will need to look back over these notes to get a better understanding of their use. During lab time we made good progress on our data structures were able to turn in two assignments. We are working our way through doubly linked lists currently. Testing in our http server is going pretty slow, but I think we are getting there slowly but surely. Don't call me Shirley."}
]


@view_config(route_name="home", renderer="templates/home.jinja2")
def home_view(request):
    """Returns home page of learning journal."""
    return {"entries": ENTRIES}


@view_config(route_name="detail", renderer="templates/detail.jinja2")
def detail_view(request):
    """Returns detail page for an entry in learning journal."""
    for entry in ENTRIES:
        if entry['id'] == int(request.matchdict['id']):
            return entry


@view_config(route_name="create", renderer="templates/create.jinja2")
def create_view(request):
    """Returns a blank entry page to add entry to learning journal."""
    return {"entries": ENTRIES}


@view_config(route_name="update", renderer="templates/edit.jinja2")
def update_view(request):
    """Returns entry to be edited in the learning journal."""
    for entry in ENTRIES:
        if entry['id'] == int(request.matchdict['id']):
            return entry
