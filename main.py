from utils.file_utils import get_colleagues_list
from utils.openspace import Openspace
from utils.table import Table

openspace1 = Openspace([Table(4) for _ in range(6)])
colleagues = get_colleagues_list(input("Enter the file path"))
openspace1.organize(colleagues)
openspace1.display()

