(ns adventofclojure.day-02-test
  (:require [clojure.test :refer :all]
            [adventofclojure.day-02 :refer :all]))

(deftest solve-test
  (testing "part 1"
    (is (= "1985" (first (solve "ULL\nRRDDD\nLURDL\nUUUUD")))))
  (testing "part 2"
    (is (= "5DB3" (second (solve "ULL\nRRDDD\nLURDL\nUUUUD"))))))
