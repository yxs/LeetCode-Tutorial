#include <cstdio>

int main()
{
    int t;
    // https://en.cppreference.com/w/cpp/language/types
    // usually (in bytes)
    // short 2, int 4, long 8, float 4, double 8, char 1, w_char 2 or 4
    long long a, b, c;
    scanf("%d", &t);
    for (int i = 0; i != t; ++i)
    {
        scanf("%lld%lld%lld", &a, &b, &c);
        printf("Case #%d: %s\n", i + 1, a + b > c ? "true" : "false");
    }
    return 0;
}
