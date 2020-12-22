(ns adventofcode2018.day01-test
  (:require [clojure.test :refer :all]
            [adventofcode2018.day01 :refer :all]))

(defn reset-vars []
  (reset! seen [])
  (reset! result 0)
  (reset! counter 0))

(deftest day-01-test
  (testing "Day 01. Part 1"
    (is (= (my_frequency [1 -2 3 1]) 3))
    (is (= (my_frequency [1 1 1]) 3))
    (is (= (my_frequency [1 1 -2]) 0))
    (is (= (my_frequency [-1 -2 -3]) -6))
    (is (= (my_frequency input) 477)))
  (testing "Day 01. Part 2"
    (is (= (my_occurrence [1 -1]) 0))
    (reset-vars)
    (is (= (my_occurrence [3 3 4 -2 -4]) 10))
    (reset-vars)
    (is (= (my_occurrence [-6 3 8 5 -6]) 5))
    (reset-vars)
    (is (= (my_occurrence [7 7 -2 -7 -4]) 14))
    (reset-vars)
    (is (= (my_occurrence input) 390))))
