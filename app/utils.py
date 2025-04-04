#for reusable logic and functions; define them here

import random

def get_animal_choices(data):
    player_action = data["animal"]
    possible_actions = ["bee", "bun", "corvid", "cat", "wolf", "human"]
    computer_action = random.choice(possible_actions)
    return player_action, computer_action

def random_button():
    possible_buttons = ["Let's go!", "It's on!", "Cower before me!", "You're too weak!", "I'm scared!"]
    button_dialogue = random.choice(possible_buttons)
    return button_dialogue

def outcome(player_action, computer_action):
    print("outcome function is working")

    if player_action == "bee":
        if computer_action == "bee":
            outcome = "Tie"
        elif computer_action == "bun":
            outcome = "In a battle for territory, where the prize is a meadow full of flowers that are both great for buns to eat and hide from predators and for bees to siphon nectar, the bun calls in reinforcements. Soon, there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers, eating too many for your colony to sustain. You lose!\n"
        elif computer_action == "corvid":
            outcome = "The corvid eats you. You lose!\n"
        elif computer_action == "cat":
            outcome = "Despite a well calculated swat, you outmanuerver the cat and manage to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "wolf":
            outcome = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        else:
            humanandbee_win_or_lose_actions = [
                ("The human is allergic to your sting and is hospitalized. You win!\n", "win")
                ("The human smacks you with a newspaper, crushing you immediately. You lose!\n", "lose")
            ]
            computer_action_bee_vs_human = random.choice(humanandbee_win_or_lose_actions)
            outcome = computer_action_bee_vs_human
    elif player_action == "bun":
        if computer_action == "bee":
            outcome = "Your ears flick as the sound of buzzing fills their tunneling canals. You're able to pinpoint just where it's coming from, and just where it's going. With one impressive hop, and a well timed kick with your large fluffy feet, you kick the bee out of the air and send it spiraling back from whence it came. You win!\n"
        elif computer_action == "bun":
            outcome = "Tie"
        elif computer_action == "corvid":
            outcome = "The corvid sees you outside of your den and alerts your presence to nearby wolves. You are hunted, and both wolf and corvid enjoy the meal. You lose!\n"
        elif computer_action == "cat":
            outcome = "The cat, brought in as pest control, drives you and your family from the garden you've lived in from birth. You lose!\n"
        elif computer_action == "wolf":
            outcome = "The wolf takes chase after you, but you're too fast and you make it back to the den before you can be claimed as dinner. The wolf must go hungry this time. You win!\n"
        else:
            humanandbun_win_or_lose_actions = [
                ("The human unknowingly plants a garden of lettuce and tomatoes ontop of an underground bunny tunnel system, allowing you and your family easy access to the human's produce while being difficult to find and exterminate. You win!\n", "win")
                ("The human lays traps that ensnare you and your kin. You lose!\n", "lose")
            ]
            computer_action_bun_vs_human = random.choice(humanandbun_win_or_lose_actions)
            outcome = computer_action_bun_vs_human
    elif player_action == "corvid":
        if computer_action == "bee":
            outcome = "With your vast intelligence and tool-making abilities, you use a stick to pry bees and larvae from their hive for a quick snack while using your flight and agility to avoid their stings. You win!\n"
        elif computer_action == "bun":
            outcome = "Corvid eats the bee. You lose!\n"
        elif computer_action == "corvid":
            outcome = "Tie"
        elif computer_action == "cat":
            outcome = "Despite a well calculated swat, the bee outmanuervers the cat and manages to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "wolf":
            outcome = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        else:
            humanandcorvid_win_or_lose_actions = [
                ("Human destroys the corvid's natural habitat and it's forced to live in the city. You lose!\n", "lose") 
                ("Human enters the world of Alfred Hitchcock's *The Birds* and has their eyes pecked out by a crazed corvid. You win!\n", "win")
            ]
            computer_action_corvid_vs_human = random.choice(humanandcorvid_win_or_lose_actions)
            outcome = computer_action_corvid_vs_human
    elif player_action == "cat":
        if computer_action == "bee":
            outcome = "In a battle for territory where the prize is land full of flowers which are great for hiding from predators, as wells as siphoning nectar, the bun calls in reinforcements and quickly there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers. You lose!\n"
        elif computer_action == "bun":
            outcome = "Corvid eats the bee. You lose!\n"
        elif computer_action == "corvid":
            outcome = "Despite a well calculated swat, the bee outmanuervers the cat and manages to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "cat":
            outcome = "Tie"
        elif computer_action == "wolf":
            outcome = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        else:
            humanandcat_win_or_lose_actions = [
                ("Human domesticates the cat and makes it wear silly hats and posts pictures of the embarassing situation all over the internet. You lose!\n", "lose") 
                ("Human is infected with toxoplasmosis and becomes a slave to the cat. You win!\n", "win")
            ]
            computer_action_cat_vs_human = random.choice(humanandcat_win_or_lose_actions)
            outcome = computer_action_cat_vs_human
    elif player_action == "wolf":
        if computer_action == "bee":
            outcome = "In a battle for territory where the prize is land full of flowers which are great for hiding from predators, as wells as siphoning nectar, the bun calls in reinforcements and quickly there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers. You lose!\n"
        elif computer_action == "bun":
            outcome = "Corvid eats the bee. You lose!\n"
        elif computer_action == "corvid":
            outcome = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        elif computer_action == "cat":
            outcome = "Despite a well calculated swat, the bee outmanuervers the cat and manages to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "wolf":
            outcome = "Tie"
        else:
            humanandwolf_win_or_lose_actions = [
                ("Human tests the wolf's boundaries with a meat-suit and gets mauled. You win!\n", "win")
                ("Human confuses coyotes killing their livestock for wolves and goes on a mass hunting spree. You lose!\n", "lose")
            ]
            computer_action_wolf_vs_human = random.choice(humanandwolf_win_or_lose_actions)
            outcome = computer_action_wolf_vs_human
    elif player_action == "human":
        if computer_action == "bee":
            bee_win_or_lose_actions = [
                ("Bee does a little dance that rallies the masses to attack the human. You lose!\n", "lose")
                ("Human makes a movie about the bee that makes everyone assume it likes Jazz. It hears 'Ya like jazz?' for the remainder of its life. You win!\n", "win")
            ]
            computer_action_human_vs_bee = random.choice(bee_win_or_lose_actions)
            outcome = computer_action_human_vs_bee
        elif computer_action == "bun":
            bun_win_or_lose_actions = [
                ("Bun, and its family, enjoys a very large meal which, to the human's dismay, turns out to be their crop yeild for the season. You lose!\n", "lose")
                ("Bun foregoes it's usual choice of lettuce, and other mediocre looking vegetables, for some unusually juicy and delicious looking tomatoes. Turns out the reason they looked so good was because of DDT. The bun is poisoned and no longer bothers any of the crops. You win!\n", "win")
            ]
            computer_action_human_vs_bun = random.choice(bun_win_or_lose_actions)
            outcome = computer_action_human_vs_bun
        elif computer_action == "corvid":
            corvid_win_or_lose_actions = [
                ("Corvid drops from the sky due to human neonicotinoids. Well, at least the bugs are gone from the apples. You win!\n", "win")
                ("Corvid waits for human to turn its head then attacks while its not looking, you lose!\n", "lose")
            ]
            computer_action_human_vs_corvid = random.choice(corvid_win_or_lose_actions)
            outcome = computer_action_human_vs_corvid
        elif computer_action == "cat":
            cat_win_or_lose_actions = [
                ("Human adopts the cat and realizes putting forth effort for another individual is too much. The cat is dumped in the street. You win!\n", "win")
                ("Cat, while being driven out of its home by someone who can no longer provide for it, turns and mauls the human with claws of fury before finding a better home elsewhere. You lose!\n", "lose")
            ]
            computer_action_human_vs_cat = random.choice(cat_win_or_lose_actions)
            outcome = computer_action_human_vs_cat
        elif computer_action == "wolf":
            wolf_win_or_lose_actions = [
                ("Human retracts laws against indiscriminatory hunting of wolves. Wolves go extinct and species that require a keystone species destroy the ecosystem. You win!\n", "win")
                ("Human attempts to hunt a wolf and instead meets the whole pack. The human is out of ammo. You lose!\n", "lose")
            ]
            computer_action_human_vs_wolf = random.choice(wolf_win_or_lose_actions)
            outcome = computer_action_human_vs_wolf
        else:
            outcome = "This is human vs human which are both wild cards, this will be substantially different from the function we've made."
    else:
        raise ValueError(f"Unexpected input: player={player_action}, computer={computer_action}")
    
    return outcome