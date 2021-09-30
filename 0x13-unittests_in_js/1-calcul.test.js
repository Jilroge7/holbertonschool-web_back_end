const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('#calculateNumber()', function () {
  it('should return 4 when 1 and 3 is passed and added', function () {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
  });
  it('should return 5 when 1 and 3.7 is passed and added', function () {
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('should return 5 when 1.2 and 3.7 is passed and added', function () {
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('should return 6 when 1.5 and 3.7 is passed and added', function () {
    assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
  });
  it('should return 3 when -1 and 3.7 is passed and added', function () {
    assert.equal(calculateNumber('SUM', -1, 3.7), 3);
  });
  it('should return 0 when 0.1 and 0.3 is passed and added', function () {
    assert.equal(calculateNumber('SUM', 0.1, 0.3), 0);
  });
  it('should return -5 when -1 and -3.7 is passed and added', function () {
    assert.equal(calculateNumber('SUM', -1, -3.7), -5);
  });
  it('should return -2 when 1 and 3 is passed and subtracted', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
  });
  it('should return 3 when 3.7 and 1 is passed and subtracted', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 3.7, 1), 3);
  });
  it('should return 3 when 3.7 and 1.2 is passed and subtracted', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 3.7, 1.2), 3);
  });
  it('should return 2 when 3.7 and 1.5 is passed and subtracted', function () {
    assert.equal(calculateNumber('SUBTRACT', 3.7, 1.5), 2);
  });
  it('should return -5 when -1 and 3.7 is passed and subtracted', function () {
    assert.equal(calculateNumber('SUBTRACT', -1, 3.7), -5);
  });
  it('should return 0 when 0.1 and 0.3 is passed and subtracted', function () {
    assert.equal(calculateNumber('SUBTRACT', 0.1, 0.3), 0);
  });
  it('should return 3 when -1 and -3.7 is passed and subtracted', function () {
    assert.equal(calculateNumber('SUBTRACT', -1, -3.7), 3);
  });
  it('should return 3 when 3 and 1 is passed and divided', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 3, 1), 3);
  });
  it('should return 0.2 when 1.4 and 4.5 is passed and divided', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it('should return Error when 1.4 and 0 is passed and divided', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
