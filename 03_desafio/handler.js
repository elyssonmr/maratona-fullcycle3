'use strict';

module.exports.sum = async event => {
  let params = event.queryStringParameters

  let result = parseInt(params.a) + parseInt(params.b)
  
  return {
    statusCode: 200,
    body: JSON.stringify({resultado: result}, null, 2)
  }
};
