import random

# lists of elements for generating plots
characters = ["Captain Kirk", "Spock", "Dr. McCoy", "Lt. Uhura", "Scotty", "Chekov", "Sulu", "Captain Pike", "Number One", "Captain Picard", "Commander Riker", "Worf", "Lt. Data", "Dr. Crusher", "Dr. Pulaski", "Tasha Yar", "Wesley Crusher", "Troi", "La Forge", "Captain Sisko", "Kira Nerys", "Garak", "Quark", "Odo", "Nog", "Jake Sisko", "Gul Dukat", "Jadzia Dax", "Ezri Dax", "Dr. Bashir", "O'Brien", "Captain Janeway", "The Doctor", "Chakotay", "Tuvok", "Neelix", "Kes", "Seven of Nine", "Lt. Torres", "Lt. Paris", "Harry Kim", "Captain Archer", "Dr. Phlox", "T'Pol", "Reed", "Mayweather", "Sato", "Trip", "Captain Burnham", "Saru", "Paul Stamets", "Tilly", "Culber", "Tyler", "Nhan", "Adira", "Jett Reno", "Christine Chapel", "La'an", "Lt. Ortegas", "Dr. M'Benga", "Hemmer"]
alien_species = ["Klingons", "Romulans", "Borg", "Vulcans", "Andorians", "Ferengi", "alternate universe humans", "members of Section 31", "Cardassians", "Bajorans", "Dominion", "Founders", "Q", "Xindi"]
plot_actions = ["encounters", "investigates", "rescues", "negotiates with", "explores", "battles against", "falls in love with", "is infected by"]
locations = ["an unknown planet", "a space station", "an asteroid field", "a nebula", "a derelict ship", "an alternate timeline"]
conflicts = ["a misunderstanding", "a diplomatic crisis", "a natural disaster", "a technological malfunction", "a minor disagreement"]
resolutions = ["by finding common ground", "through sacrifice", "with the help of an unexpected ally", "by outsmarting the enemy", "by escaping with their lives intact", "with copious amounts of drugs", "with planet-destroying weapons"]
ships = ["the USS Enterpise", "the USS Enterprise-D", "the USS Defiant", "Deep Space Nine", "the USS Voyager", "the USS Discovery", "the USS Cerritos", "the USS Protostar"]

# generate a random plot
def generate_plot():
    character = random.choice(characters)
    action = random.choice(plot_actions)
    species = random.choice(alien_species)
    location = random.choice(locations)
    conflict = random.choice(conflicts)
    resolution = random.choice(resolutions)
    ship = random.choice(ships)
    return f"{character}, alongside the crew of {ship} {action} the {species} at {location} due to {conflict}, and must resolve the situation {resolution}."

# generate multiple plots
def generate_plots(num_plots):
    plots = []
    for _ in range(num_plots):
        plots.append(generate_plot())
    return plots

# number of plots to generate
if __name__ == "__main__":
    num_plots = int(input("Boldly go how many places? "))
    plots = generate_plots(num_plots)
    for i, plot in enumerate(plots, 1):
        print(f"Episode {i}: {plot}")
