(ns adventofcode2018.day05-test
  (:require [clojure.test :refer :all]
            [adventofcode2018.day05 :refer :all]))

(deftest day-05-test
  (testing "Day 05. Part 1"
    (is (= (reduction "aA") ""))
    (is (= (reduction "abBA") ""))
    (is (= (reduction "abAB") "abAB"))
    (is (= (reduction "aabAAB") "aabAAB"))
    (is (= (reduction "dabAcCaCBAcCcaDA") "dabCBAcaDA"))
    (is (= (polymer "dabAcCaCBAcCcaDA") 10)))
  (testing "Day 05. Part 2"
    (is (= (shortest-polymer "dabAcCaCBAcCcaDA") 4))))
