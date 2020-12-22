(ns adventofcode2018.day02-test
  (:require [clojure.test :refer :all]
            [adventofcode2018.day02 :refer :all]))

(def test-input ["abcdef"                ;; 2*0 3*0
                 "bababc"                ;; 2*1 3*1
                 "abbcde"                ;; 2*1 3*0
                 "abcccd"                ;; 2*0 3*1
                 "aabcdd"                ;; 2*0 3*1
                 "abcdee"                ;; 2*2 3*1
                 "ababab"])              ;; 2*0 3*0

(deftest day-02-test
  (testing "Day 02. Part 1"
    (is (= (checksum test-input) 12))
    (is (= (checksum input) 5952)))
  (testing "Day 02. Part 2"
    (is (= 0 "krdmtuqjgwfoevnaboxglzjph"))))