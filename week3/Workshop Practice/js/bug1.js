var accounts = {
    a: 120,
    b: 0,
    c: 30
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
        accounts[accountName] += amount;
    }
}

transfer("a", "c", 20);
deposit("b", 150);
transfer("b", "c", 50);


