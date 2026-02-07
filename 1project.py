import random

print("pick number: 1, 2 or 3")
template_number = input()

if template_number == "": 
    template_number = random.choice(["1", "2", "3"])
if template_number == "1":
    print("input number")
    Number = input()

    print("input Measure of time")
    Measure_of_time = input()

    print("input Mode of Transportation")
    Mode_of_Transportation = input()

    print("input Adjective")
    Adjective = input()

    print("input Adjective")
    Adjective2 = input()

    print("input Noun")
    Noun = input()

    print("input Color")
    Color = input()

    print("input Part of the Body")
    Part_of_the_Body = input()

    print("input Verb")
    Verb = input()

    print("input number")
    Number2 = input()

    print("input Noun")
    Noun2 = input()

    print("input Noun")
    Noun3 = input()

    print("input Part of the Body")
    Part_of_the_Body_2 = input()

    print("input Verb")
    Verb2 = input()

    print("input Noun")
    Noun4 = input()

    print("input Adjective")
    Adjective3 = input()

    print("input Silly Word")
    Silly_Word = input()

    print("It was about", Number, Measure_of_time, "ago when I arrived at the hospital in a", Mode_of_Transportation,". The hospital is a/an", Adjective, "place, there are a lot of", Adjective2, Noun, "here. There are nurses here who have", Color, Part_of_the_Body, ". If someone wants to come into my room I told them that they have to", Verb, "first. I’ve decorated my room with",Number2, Noun2, ". Today I talked to a doctor and they were wearing a", Noun3, "on their", Part_of_the_Body_2, ". I heard that all doctors", Verb2, Noun4, "every day for breakfast. The most",Adjective3, "thing about being in the hospital is the", Silly_Word, Noun, "!")
    

elif template_number == "2":
    print("input Proper Noun (Person’s Name)")
    Proper_Noun_Name = input()

    print("input Noun")
    Noun = input()

    print("input Adjective (Feeling)")
    Adjective_Feeling = input()

    print("input Verb")
    Verb = input()

    print("input Adjective (Feeling)")
    Adjective_Feeling_2 = input()

    print("input Animal")
    Animal = input()

    print("input Verb")
    Verb2 = input()

    print("input Color")
    Color = input()

    print("input Verb (ending in ing)")
    Verb_ending_in_ing = input()

    print("input Adverb (ending in ly)")
    Adverb_ending_in_ly = input()

    print("input Number")
    Number = input()

    print("input Measure of time")
    Measure_of_time = input()

    print("input Color")
    Color2 = input()

    print("input Animal")
    Animal2 = input()

    print("input Number")
    Number2 = input()

    print("input Silly Word")
    Silly_Word = input()

    print("input Noun")
    Noun2 = input()

    print("This weekend I am going camping with", Proper_Noun_Name, ". I packed my lantern, sleeping bag, and", Noun, ". I am so", Adjective_Feeling, "to", Verb, "in a tent. I am", Adjective_Feeling_2, "we might see a(n)", Animal , ", I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and", Verb2, ". I have heard that the", Color,  "lake is great for",Verb_ending_in_ing, ". Then we will", Adverb_ending_in_ly, "hike through the forest for", Number, Measure_of_time, ". If I see a", Color2, Animal2, "while hiking, I am going to bring it home as a pet! At night we will tell",Number2, Silly_Word, "stories and roast", Noun2, "around the campfire!!")
    

elif template_number == "3":
    print("input Proper Noun (Person’s Name)")
    Proper_Noun_Name = input()

    print("input Adjective")
    Adjective = input()

    print("input Color")
    Color = input()

    print("input Animal")
    Animal = input()

    print("input Place")
    Place = input()

    print("input Adjective")
    Adjective2 = input()

    print("input Magical Creature (Plural)")
    Magical_Creature_Plural = input()

    print("input Adjective")
    Adjective3 = input()

    print("input Magical Creature (Plural)")
    Magical_Creature_Plural_2 = input()

    print("input Room in a House")
    Room_in_a_House = input()

    print("input Noun")
    Noun = input()

    print("input Noun")
    Noun2 = input()

    print("input Noun (Plural)")
    Noun_Plural_3 = input()

    print("input Adjective")
    Adjective4 = input()

    print("input Noun (Plural)")
    Noun_Plural_4 = input()

    print("input Number")
    Number = input()

    print("input Measure of time")
    Measure_of_time = input()

    print("input Verb (ending in ing)")
    Verb_ending_in_ing = input()

    print("input Adjective")
    Adjective5 = input()

    print("input Noun")
    Noun5 = input()

    print("Dear", Proper_Noun_Name, "I am writing to you from a", Adjective, "castle in an enchanted forest. I found myself here one day after going for a ride on a", Color, Animal, "in", Place, ". There are", Adjective2, Magical_Creature_Plural, "and", Adjective3, Magical_Creature_Plural_2, "here! In the", Room_in_a_House, "there is a pool full of", Noun, ". I fall asleep each night on a", Noun2, "of", Noun_Plural_3, "and dream of", Adjective4, Noun_Plural_4, ". It feels as though I have lived here for", Number, Measure_of_time, ". I hope one day you can visit, although the only way to get here now is", Verb_ending_in_ing, "on a", Adjective5, Noun5, "!!")

else:
    print("wrong number")










