#include "main.h"
#include <gtest/gtest.h>

TEST(MyTests, test1)
{
    ASSERT_FALSE(less(2,1));
    for(int i = 0; i < 99; i++) {
        ASSERT_TRUE(less(0, 1));
    }
}


TEST(MyTests, test2)
{
    ASSERT_EQ(7, Sum(3, 4));
    ASSERT_EQ(12, Sum(5, 7));
}
