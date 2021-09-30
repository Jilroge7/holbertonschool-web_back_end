const assert = require('assert');
const calculateNumber = require('./2-calcul_chai');

describe('#calculateNumber() and type is SUM', function () {
  it('should return 4 when 1 and 3 is passed and added', function () {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
  });
  it('should return 5 when 1 and 3.7 is passed and added', function () {
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
  });
  it('should return 5 when 1.2 and 3.7 is passed and added', function () {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
  });
  it('should return 6 when 1.5 and 3.7 is passed and added', function () {
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
  });
  it('should return 3 when -1 and 3.7 is passed and added', function () {
    expect(calculateNumber('SUM', -1, 3.7)).to.equal(3);
  });
  it('should return 0 when 0.1 and 0.3 is passed and added', function () {
    expect(calculateNumber('SUM', 0.1, 0.3)).to.equal(0);
  });
  it('should return -5 when -1 and -3.7 is passed and added', function () {
    expect(calculateNumber('SUM', -1, -3.7)).to.equal(-5);
  });
});

describe('#calculateNumber() and type is SUBTRACT', function () {
  it('should return -2 when 1 and 3 is passed and subtracted', function () {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
  });
  it('should return 3 when 3.7 and 1 is passed and subtracted', function () {
    expect(calculateNumber('SUBTRACT', 3.7, )).to.equal(3);
  });
  it('should return 3 when 3.7 and 1.2 is passed and subtracted', function () {
    expect(calculateNumber('SUBTRACT', 3.7, 1.2)).to.equal(3);
  });
  it('should return 2 when 3.7 and 1.5 is passed and subtracted', function () {
    expect(calculateNumber('SUBTRACT', 3.7, 1.5)).to.equal(2);
  });
  it('should return -5 when -1 and 3.7 is passed and subtracted', function () {
    expect(calculateNumber('SUBTRACT', -1, 3.7)).to.equal(-5);
  });
  it('should return 0 when 0.1 and 0.3 is passed and subtracted', function () {
    expect(calculateNumber('SUBTRACT', 0.1, 0.3)).to.equal(0);
  });
  it('should return 3 when -1 and -3.7 is passed and subtracted', function () {
    expect(calculateNumber('SUBTRACT', -1, -3.7)).to.equal(3);
  });
});

describe('#calculateNumber() and type is DIVIDE', function () { 
  it('should return 3 when 3 and 1 is passed and divided', function () {
    expect(calculateNumber('DIVIDE', 3, 1)).to.equal(3);
  });
  it('should return 0.2 when 1.4 and 4.5 is passed and divided', function () {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it('should return Error when 1.4 and 0 is passed and divided', function () {
    expect(calculateNumber('DIVIDE', 1.4, 0), ).to.equal('Error');
  });
});
