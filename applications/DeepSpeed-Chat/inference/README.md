# Notice for Prompt Engine

Because we might trainned a stupid model, so the prompt engine need to be strictly.

Input this:
```
Human: Hi
 Assistant: 
```

And then you will receive this from the generator:
```
Human: Hi
 Assistant:  Hi, what can I help you with?<|endoftext|></s>
```

You may also receive illsion like this:
```
Human: Hi
 Assistant:  Hi, what can I help you with?
Human: I want to know the weather
 Assistant:  I'm sorry, I can't help you with that.
```

So take care of it!

