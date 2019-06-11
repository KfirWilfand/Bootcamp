var accounts = {
    a: 150,
    b: 50,
    c: 50
};

function getAccount(accountName) {
    if (!accounts.hasOwnProperty(accountName)) {
        throw new Error("No such account: " + accountName);
    }
    return accounts[accountName];
}

function transfer(from, to, amount) {
    if (getAccount(from) < amount) return;
    accounts[from] -= amount;
    accounts[to] += amount;
}

function deposit(accountName, amount) {
    var account = getAccount(accountName);
    if (account) {
        account += amount;
    }
}

transfer("a","c",50);
deposit("b", 50);

// what is the bug?