from botanical import Botanical

def reason(problem: str, max_iterations: int = 10) -> str:
    bot = Botanical()
    
    bot.call(f"Problem: {problem}")
    
    for i in range(max_iterations - 1):
        if bot.is_complete():
            break
        bot.call("continue")
    
    return bot.decode()


if __name__ == "__main__":
    result = reason("What is the best data structure for a priority queue?")
    print(result)
