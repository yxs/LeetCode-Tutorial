队列实现栈，单队列即可，每次入队后，将前 queue.size() - 1 个元素一次重新入队并 pop 掉

```cpp
    void push(int x)
    {
        q.push(x);
        for (int i = 1; i < q.size(); ++i)
        {
            q.push(q.front());
            q.pop();
        }
    }
```

栈实现队列，元素push到input栈，需要取队首元素时，
1. 返回output栈顶元素
2. 若output栈为空，依次取input栈顶，入栈到output栈

```cpp
    /** Get the front element. */
    int peek()
    {
        if (output.empty())
        {
            while (input.size())
            {
                output.push(input.top());
                input.pop();
            }
        }
        return output.top();
    }
```