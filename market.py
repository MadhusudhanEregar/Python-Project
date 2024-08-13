class User:
    def __init__(self, user_id, name, skills, experience, contact):
        self.user_id = user_id
        self.name = name
        self.skills = skills
        self.experience = experience
        self.contact = contact
        self.skill_gap = []

class Organization:
    def __init__(self, org_id, name, users):
        self.org_id = org_id
        self.name = name
        self.users = users

# Create user instances
user1 = User(1, "Siddarth", ["C", "Java", "C++"], 3, 5243566477)
user2 = User(2, "Ashok", ["Java", "python", "C"], 5, 8746643664)
user3 = User(3, "Madhusudhan", ["python", "C", "Java"], 2, 7346575244)
user4 = User(4, "Shreyas", ["python", "Java", "C", "C++"], 6, 747673823)
user5 = User(5, "Mallikarjun", ["C", "python", "C++"], 3, 6467374745)
user6 = User(6, "Kiran", ["python", "Java", "C++"], 2, 6546576778)
user7 = User(7, "Akshay", ["Java", "C", "C++"], 3, 6774375644)
user8 = User(8, "Ajeeth", ["python", "C", "C++"], 4, 9473987565)

# Create organization instances
org1 = Organization(101, "TechCorp", [user1, user2])
org2 = Organization(102, "DataCo", [user3, user4])
org3 = Organization(103, "Infosis", [user5, user6])
org4 = Organization(104, "Vertex", [user7, user8])

def is_valid_skill(skill):
    return skill.isalpha()  # Check if the skill contains only alphabetic characters

def display_required_skills():
    print("Required skills:\n1. Python\n2. Java\n3. C\n4. C++")

def select_skill():
    while True:
        skills_input = input("Enter skills (comma separated): ").split(",")
        skills = [skill.strip().lower() for skill in skills_input]
        
        if all(is_valid_skill(skill) for skill in skills):
            break
        else:
            print("Invalid input. Please enter skills containing only alphabetic characters.")
    
    matching_users = []
    unmatching_users = []
    
    for org in [org1, org2, org3, org4]:
        for user in org.users:
            if all(skill.lower() in map(str.lower, user.skills) for skill in skills):
                matching_users.append(user)
            else:
                user.skill_gap = list(set(skills) - set(map(str.lower, user.skills)))
                unmatching_users.append(user)
    
    return matching_users, unmatching_users

def display_users(users):
    for user in users:
        print(f'User ID: {user.user_id}, Name: {user.name}')

def display_user_profile(user_id):
    all_users = [user for org in [org1, org2, org3, org4] for user in org.users]
    user = next((u for u in all_users if u.user_id == user_id), None)
    if user:
        print(f"\nUser ID: {user.user_id}\nName: {user.name}\nSkills: {', '.join(user.skills)}\nExperience: {user.experience} years\nContact: {user.contact}")
        if user.skill_gap:
            print(f'Skill Gap: {", ".join(user.skill_gap)}')
    else:
        print("User not found")

menu_flag = True
while True:
    print("\nMenu:")
    print("1. Select the user for a project")
    print("2. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        display_required_skills()
        matching_users, unmatching_users = select_skill()
        print("Users with selected skills:")
        display_users(matching_users)
        
        while menu_flag:
            print("\nSecond Menu:")
            print("1. Select user ID")
            print("2. Skill Gap")
            print("3. Back to main menu")
            second_choice = input("Enter your choice: ")
            
            if second_choice == '1':
                user_id = int(input("Enter the user ID to display profile: "))
                display_user_profile(user_id)
            elif second_choice == '2':
                print("\nSkill Gap:")
                display_users(unmatching_users)
            elif second_choice == '3':
                menu_flag = False
            else:
                print("Invalid choice. Please try again.")
        
        menu_flag = True  # Reset menu_flag to True after exiting the second menu
    
    elif choice == '2':
        break
    
    else:
        print("Invalid choice. Please try again.")
