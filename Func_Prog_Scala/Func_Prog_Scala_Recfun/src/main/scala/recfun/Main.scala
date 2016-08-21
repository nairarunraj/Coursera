package main.scala.recfun

object Main {
  var pascalTriangle = scala.collection.mutable.HashMap.empty[String, Int]

  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = {
    var positionKey = c + "|" + r
    if (pascalTriangle contains positionKey) return pascalTriangle(positionKey)
    if (c == 0 || c == r) {
      pascalTriangle += (positionKey -> 1)
    } else {
      val positionValue = pascal(c - 1, r - 1) + pascal(c, r - 1)
      pascalTriangle += (positionKey -> positionValue)
    }
    pascalTriangle(positionKey)
  }

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {
    def innerBalance(chars: List[Char], paranthesesCount: Int): Int = {
      if (chars.isEmpty || paranthesesCount < 0) paranthesesCount
      else if (chars.head.equals('(')) innerBalance(chars.tail, paranthesesCount + 1)
      else if (chars.head.equals(')')) innerBalance(chars.tail, paranthesesCount - 1)
      else innerBalance(chars.tail, paranthesesCount)
    }
    innerBalance(chars, 0) == 0
  }

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    if (money == 0)
      1 // Only one way in not giving money
    else if (money > 0 && !coins.isEmpty)
      // number of ways using the first coin + number of ways with the rest of the coins
      countChange(money - coins.head, coins) + countChange(money, coins.tail)
    else
      0 // money is -ve or coins have exhausted
  }
}
