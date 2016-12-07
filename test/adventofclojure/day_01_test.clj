(ns adventofclojure.day-01-test
  (:require [clojure.test :refer :all]
            [adventofclojure.day-01 :refer :all]))

(deftest move-test
  (is (=  {:dir :n, :n 1, :s 0, :e 0, :w 0} (move starting-state "X1"))))

(deftest turn-test
  (is (=  {:dir :n, :n 0, :s 0, :e 0, :w 0} (turn starting-state "X0")))
  (is (=  {:dir :w, :n 0, :s 0, :e 0, :w 0} (turn starting-state "L0")))
  (is (=  {:dir :e, :n 0, :s 0, :e 0, :w 0} (turn starting-state "R0"))))

(deftest add-crumb-test
  (is (= {:dir :n, :n 1, :s 0, :e 1, :w 0, :crumbs '({:x 1, :y 1} {:x 0, :y 0})}
         (add-crumb {:dir :n, :n 1, :s 0, :e 1, :w 0, :crumbs '({:x 0, :y 0})}))))

(deftest revisited-test
  (is (= true (revisited? {:dir :n, :n 1, :s 0, :e 1, :w 0, :crumbs '({:x 1, :y 1} {:x 1, :y 1})})))
  (is (= false (revisited? {:dir :n, :n 1, :s 0, :e 1, :w 0, :crumbs '({:x 1, :y 1} {:x 0, :y 0})}))))

(deftest taxicab-distance-test
  (is (= 0 (taxicab-distance starting-state)))
  (is (= 4 (taxicab-distance {:dir :n, :n 1, :s 3, :e 3, :w 1}))))

(deftest solve-test
  (testing "part 1"
    (is (=  5 (first (solve "R2, L3"))))
    (is (=  2 (first (solve "R2, R2, R2"))))
    (is (= 12 (first (solve "R5, L5, R5, R3")))))
  (testing "part 2"
    (is (=  4 (second (solve "R8, R4, R4, R8"))))))
