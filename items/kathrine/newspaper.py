from item import Item

class Newspaper(Item):

  def __init__(self):
    self.id = 'Kathrine.newspaper'
    self.name = 'Newspaper'
    self.description = "Today's newspaper. You can 'read' it."

  def do(self, player, command):
    if command == 'read newspaper'or command=='read' or command=='read paper':

      article = """
Attitudes towards COVID-19 vaccines seem to be improving in some parts of the world, a survey of thousands of people in 15 countries has found. Researchers have welcomed the results, which suggest that an increasing proportion of people are willing to be immunized. But they caution that some problems persist, such as concerns about vaccine safety.

“For the first time since the pandemic began, I can sense that optimism is spreading faster than the virus,” says behavioural scientist Sarah Jones at Imperial College London, who co-led the global attitudes towards a COVID-19 vaccine survey.

The survey is part of the COVID-19 behaviour tracker, run by Imperial together with the UK market-research company YouGov. It ran from November 2020 to January 2021, polling around 13,500 people across Europe, Asia and Australia each time. In November — before countries began to approve COVID-19 vaccines — only around 40% of respondents said they would get a COVID-19 vaccine if they were offered one during the week that they took the survey, and more than half were worried about potential side effects. “It was very important to us to see how attitudes were changing” once national roll-outs started, says Melanie Leis, a policy researcher at Imperial College London who co-led the project.

In January, more than half the respondents agreed that they would get a vaccine if it was available during the week of the survey. And the share of people who said they worry about the vaccines’ side effects had dropped to 47% (see ‘Vaccine confidence’). The United Kingdom had the highest share of people who were willing to receive a vaccine (78%) — and for 11 of the 15 countries, this figure increased, sometimes considerably. In Spain, for example, the proportion of respondents willing to be immunized had increased from 28% in November 2020 to 52% by mid-January.

Tempered optimism
“The trends are encouraging,” says Lavanya Vasudevan, a global-health researcher at Duke University in Durham, North Carolina. She adds that progress is likely to have been driven by reports of high efficacy in early vaccine candidates, and their promising safety record so far. People’s attitudes might also have changed as their friends and family shared positive or neutral experiences after getting a shot, she says. But Vasudevan cautions that the survey results cannot be extrapolated to other regions of the world, including low- and middle-income countries, until more data become available.


How COVID vaccines are being divvied up around the world
Although the situation looks increasingly positive on a global scale, the results for some individual countries paint a more complicated picture — in particular those that have a history of vaccine mistrust. Among those surveyed in France, for example, 44% are still unwilling to receive COVID immunizations. And when asked ‘How much do you trust COVID-19 vaccines?’ 66% of respondents in Japan answered ‘not at all’ or ‘a little’.

Deborah Jones, a physician at Columbia University Irving Medical Center in New York City who worked on a COVID-19 hospital ward during the city’s peak of infections, welcomes the survey’s results. “It’s great to see that more people are now open to getting a vaccine,” she says. “But what strikes me is how many people are still hesitating. Vaccine hesitancy will slow down our return to normal."""

      print(article)
      return True      
    return False

  def is_named(self, name):
    return name == 'letter'
  

