import discord
import random 
from discord.ext import commands
import aiohttp
import typing 
import json

class CodeHelp(commands.Cog):
    def __init__(self,client):
        self.client = client;
    
    @commands.command('ask',help='ask a questions ')
    async def ask(self,ctx, result_limit: typing.Optional[int] = 1, *, term: str=None):
        if term!=None:
            answer=''
            googlequery=term
            q=googlequery.replace(" ","+")
            searchurl='https://www.google.com/search?q='+q
            print(searchurl,q)

            embed = discord.Embed(
                title ="You asked",
                description =f'{term} \n ',
                colour=random.randint(0, 0xffffff)
            )
            # print(term)
            async with aiohttp.ClientSession() as session:
                async with session.get('https://www.codegrepper.com/api/search.php', params ={"q":term}) as r :
                    result = await r.json()
                
                data=result['answers']
                answerEmbed=discord.Embed(
                    title='Answers',
                )
                for i in data:
                    # print(i)
                    # print(i['answer'])
                    ans = i['answer']
                    lang =i['language']
                    source=i['source_id']
                    answer+=f'```{lang}\n{ans}```'

                    answerEmbed.add_field(
                        name="name",
                        value=f'```{lang}\n {ans}```'+f'\n [source]({source})'
                    )
            
            # embed.set_footer(text=f'{ctx.message}')
            
            if len(answer)==0:
                notFoundEmbed=discord.Embed(
                    title="Answer Not Found",
                    description=f''' You can also contribute to this answers by intalling [codegrepper](https://www.codegrepper.com/) Extensions and marking answer when you find it
                    \n[Search yourself]({searchurl})'''
                )
                await ctx.send(embed=embed)
                await ctx.send(embed=notFoundEmbed)
                pass
            elif len(answer)>1:
                await ctx.send(embed=embed)
                await ctx.send(embed=answerEmbed)
                notGotEmbed=discord.Embed(
                title=":frowning2: Not Got Your Answer?",
                description=f''' You can also contribute to this answers by intalling [codegrepper](https://www.codegrepper.com/) Extensions and marking answer when you find it
                \n[Search yourself]({searchurl})'''
                )
                await ctx.send(embed=notGotEmbed)
                pass
            else:
                
                pass
           
        else:  
            noargEmbed=discord.Embed(
                    title="Ask Something, it can't be blank",
                    description='''
                    something expected 
                    `?ask what you want to ask`
                    '''
                )
            await ctx.send(embed=noargEmbed)
        # await ctx.send(answer)


def setup(client):
    client.add_cog(CodeHelp(client))