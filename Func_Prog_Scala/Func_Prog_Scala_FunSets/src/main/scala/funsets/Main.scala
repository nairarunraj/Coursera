package funsets

object Main extends App {
  import FunSets._
  println(contains(singletonSet(1), 2))
  println(contains(union(singletonSet(1), singletonSet(2)), 1))
}
