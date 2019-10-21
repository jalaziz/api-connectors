/**
 * Bybit API
 * ## REST API for the Bybit Exchange. 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: support@bybit.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.8
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.BybitApi) {
      root.BybitApi = {};
    }
    root.BybitApi.APIKeyInfo = factory(root.BybitApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The APIKeyInfo model module.
   * @module model/APIKeyInfo
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>APIKeyInfo</code>.
   * Get bybit server time.
   * @alias module:model/APIKeyInfo
   * @class
   */
  var exports = function() {
    var _this = this;








  };

  /**
   * Constructs a <code>APIKeyInfo</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/APIKeyInfo} obj Optional instance to populate.
   * @return {module:model/APIKeyInfo} The populated <code>APIKeyInfo</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('api_key')) {
        obj['api_key'] = ApiClient.convertToType(data['api_key'], 'String');
      }
      if (data.hasOwnProperty('user_id')) {
        obj['user_id'] = ApiClient.convertToType(data['user_id'], 'Number');
      }
      if (data.hasOwnProperty('ips')) {
        obj['ips'] = ApiClient.convertToType(data['ips'], ['String']);
      }
      if (data.hasOwnProperty('note')) {
        obj['note'] = ApiClient.convertToType(data['note'], 'String');
      }
      if (data.hasOwnProperty('permissions')) {
        obj['permissions'] = ApiClient.convertToType(data['permissions'], ['String']);
      }
      if (data.hasOwnProperty('created_at')) {
        obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
      }
      if (data.hasOwnProperty('read_only')) {
        obj['read_only'] = ApiClient.convertToType(data['read_only'], 'Boolean');
      }
    }
    return obj;
  }

  /**
   * @member {String} api_key
   */
  exports.prototype['api_key'] = undefined;
  /**
   * @member {Number} user_id
   */
  exports.prototype['user_id'] = undefined;
  /**
   * @member {Array.<String>} ips
   */
  exports.prototype['ips'] = undefined;
  /**
   * @member {String} note
   */
  exports.prototype['note'] = undefined;
  /**
   * @member {Array.<String>} permissions
   */
  exports.prototype['permissions'] = undefined;
  /**
   * @member {String} created_at
   */
  exports.prototype['created_at'] = undefined;
  /**
   * @member {Boolean} read_only
   */
  exports.prototype['read_only'] = undefined;



  return exports;
}));

