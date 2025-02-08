import sys
import warnings

from test import McqGen

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

messi_text = """
Lionel Messi, widely regarded as one of the greatest football players of all time, has left an indelible mark on the sport. His extraordinary talent, skill, and achievements have not only made him a global icon but also a symbol of excellence in football. This article provides a comprehensive overview of Messi’s life, career, and the reasons behind his status as a football legend.

Lionel Andrés Messi was born on June 24, 1987, in Rosario, Argentina, to Jorge Messi and Celia María Cuccittini. From a young age, it was clear that Messi had a natural gift for football. His passion for the game was evident as he played with his older brothers and neighborhood friends. However, Messi's early life was not without challenges. At the age of 10, Messi was diagnosed with a growth hormone deficiency that threatened his career. His parents, unable to afford the expensive treatment, sought help from Newell's Old Boys, his local club. Eventually, Messi’s potential caught the eye of FC Barcelona scouts, and at just 13 years old, he moved to Spain to join the Barcelona youth academy, La Masia.

Messi’s journey at Barcelona began in the early 2000s, where he quickly ascended through the ranks of the club’s youth teams. His extraordinary dribbling skills, vision, and goal-scoring ability set him apart from his peers. Messi made his first-team debut for Barcelona in 2004 at the age of 17, and it wasn’t long before he became an essential part of the team. His rise to prominence was rapid, and by the 2005-2006 season, Messi had secured a regular spot in the Barcelona lineup.

Over the years, Messi developed into the focal point of Barcelona’s attack. His ability to score goals, provide assists, and create opportunities for his teammates made him one of the most complete players in the world. Messi’s playing style was characterized by his dribbling ability, low center of gravity, close ball control, and vision. He possessed a rare combination of agility, speed, and technique that allowed him to weave through defenses with ease.

During his time at Barcelona, Messi helped the club win numerous titles, including multiple La Liga and UEFA Champions League titles. He was instrumental in the team’s dominance during the late 2000s and early 2010s, particularly under the management of Pep Guardiola. Messi’s ability to score goals at an unprecedented rate saw him win the prestigious Ballon d'Or (awarded to the best football player in the world) on multiple occasions. He became the top scorer in the history of La Liga and broke numerous records for both club and country.

One of Messi’s most memorable achievements at Barcelona came in the 2011-2012 season, where he scored a staggering 91 goals in a calendar year, breaking the previous record held by Gerd Müller. This incredible feat cemented his reputation as a goal-scoring machine. Throughout his career at Barcelona, Messi’s relationship with the club was symbiotic; he was not just a player but the team’s leader, talisman, and captain.

While Messi’s success at Barcelona was undeniable, his international career with Argentina was often met with disappointment. Despite being hailed as one of the greatest players of all time, Messi struggled to achieve the same level of success with his national team. Argentina reached the finals of the 2014 FIFA World Cup, but Messi and his team fell short, losing to Germany in the final. The loss was particularly painful for Messi, as he was unable to replicate his club-level success on the international stage.

However, Messi’s dedication to the national team never wavered. Over the years, he continued to lead Argentina with passion and determination. In 2015, Argentina reached the final of the Copa América, but once again, Messi was left disappointed after losing to Chile. Despite these setbacks, Messi continued to play for his country, and his commitment paid off in 2021 when Argentina won the Copa América by defeating Brazil 1-0 in the final. Messi’s performance throughout the tournament was exceptional, and he was awarded the Golden Boot for being the top scorer of the competition. The victory was a significant moment in Messi’s career, as it marked his first major international trophy with Argentina.

Messi’s playing style is a blend of artistry and athleticism. His dribbling skills are unrivaled, allowing him to glide past defenders with ease. His low center of gravity, quick acceleration, and exceptional balance enable him to change direction swiftly and evade tackles. Messi’s dribbling is often described as a work of art, as he can control the ball in tight spaces and make defenders look helpless.

In addition to his dribbling, Messi is known for his vision and creativity. He is a master at picking out passes and creating goal-scoring opportunities for his teammates. His ability to thread passes through tight spaces and set up assists is a testament to his football intelligence. Messi is also a prolific goal scorer, capable of finishing with both feet and his head. His ability to score from free kicks, long-range shots, and one-on-one situations makes him one of the most complete forwards in the game.

Messi’s versatility has also been a key factor in his success. While he initially played as a winger, he later evolved into a more central role, acting as both a creator and goal scorer. His adaptability allows him to perform in a variety of attacking positions, whether as a false nine, a playmaker, or an out-and-out forward. This flexibility, combined with his skill set, has made Messi an invaluable asset to any team he plays for.

Throughout his career, Messi has set numerous records and achieved countless milestones. He has won the Ballon d'Or multiple times, solidifying his place as one of the best footballers in history. Messi is Barcelona’s all-time top scorer, having scored over 600 goals for the club in competitive matches. He also holds the record for the most goals in La Liga and has broken numerous other records, including the most goals scored in a calendar year.

On the international stage, Messi is Argentina’s top scorer, surpassing Gabriel Batistuta in 2016. He has represented his country in four FIFA World Cups and has played in several Copa América tournaments. Messi’s international career, while often criticized for lacking major trophies, has been filled with remarkable individual performances and contributions to Argentina’s success.

In 2021, Messi’s legendary tenure at Barcelona came to an unexpected end. Due to financial difficulties and La Liga’s salary cap regulations, Barcelona was unable to renew Messi’s contract, despite both the player and the club expressing a desire to continue their relationship. As a result, Messi was forced to leave the club where he had spent over two decades of his life.

In August 2021, Messi signed a contract with Paris Saint-Germain (PSG), joining the French club on a free transfer. At PSG, Messi continued to showcase his talent, forming an attacking trio with Neymar and Kylian Mbappé. While his time at PSG has been relatively short compared to his career at Barcelona, Messi has continued to add to his already impressive collection of trophies.

Lionel Messi’s legacy is one of greatness, perseverance, and excellence. His career has been defined by an unwavering commitment to the game, a relentless pursuit of improvement, and a passion for winning. Messi’s impact on football extends beyond his on-field performances. He has inspired countless young players around the world and has shown that talent, combined with hard work and determination, can lead to success.

Messi’s humility and sportsmanship have also made him a beloved figure in the footballing world. Unlike many of his peers, Messi has remained grounded throughout his career, focusing on his love for the game rather than seeking fame or fortune. His dedication to his craft and his ability to overcome adversity have made him a role model for aspiring athletes everywhere.

Lionel Messi is not just a football player; he is an icon whose influence transcends the sport. His brilliance on the field, his countless records, and his journey from a young boy in Rosario to a global superstar have made him one of the greatest athletes of all time. As he continues to play, Messi’s impact on the world of football will be remembered for generations to come."""


def run():
    """
    Run the crew.
    """

    #user_input = input("Enter your question: ")

    inputs = {
        'input': messi_text
    }

    result = McqGen().crew().kickoff(inputs=inputs)
    print(result)

if __name__ == "__main__":
    run()