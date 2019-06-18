let assert = require("assert");
var expect = require("chai").expect;

var candyStore = {
  candies: [
    {
      name: "mint gum",
      id: "as12f",
      price: 2,
      amount: 2
    },
    {
      name: "twix",
      id: "5hd7y",
      price: 5,
      amount: 4
    }
  ],
  cashRegister: 200
};

function getCandy(candyStore, id) {
  let resCandy;

  candyStore["candies"].forEach(candy => {
    if (candy.id === id) resCandy = candy;
  });

  return resCandy;
}

function getPrice(candyStore, id) {
  let resCandy;

  candyStore["candies"].forEach(candy => {
    if (candy.id === id) resCandy = candy;
  });

  return resCandy.price;
}

function addCandy(candyStore, id, name, price) {
  candyStore["candies"].push({
    name: name,
    id: id,
    price: price,
    amount: 1
  });
}

function buy(candyStore, id) {
  let resCandy;

  candyStore["candies"].forEach(candy => {
    if (candy.id === id) resCandy = candy;
  });

  resCandy['amount']--;
  resCandy.cashRegister += resCandy.price;
  return candyStore;
}

it("find candy by id", function() {
  assert(getCandy(candyStore, "5hd7y"), candyStore["candies"][1]);
});

it("find candy by price", function() {
  assert(getPrice(candyStore, "5hd7y"), 5);
});

it("add candy", function() {
  expect(addCandy(candyStore,"dfe3", "pizza", 10), 205);
});


it("add candy", function() {
  assert(buy(candyStore, "dfe3"), 5);
});


