/*
 * Bybit API
 * ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]  
 *
 * OpenAPI spec version: 0.2.10
 * Contact: support@bybit.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * LinearSearchStopOrderResult
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-12T14:39:31.513+08:00")
public class LinearSearchStopOrderResult {
  @SerializedName("stop_order_id")
  private String stopOrderId = null;

  @SerializedName("user_id")
  private Long userId = null;

  @SerializedName("side")
  private String side = null;

  @SerializedName("symbol")
  private String symbol = null;

  @SerializedName("order_type")
  private String orderType = null;

  @SerializedName("price")
  private Double price = null;

  @SerializedName("qty")
  private Double qty = null;

  @SerializedName("time_in_force")
  private String timeInForce = null;

  @SerializedName("order_status")
  private String orderStatus = null;

  @SerializedName("trigger_price")
  private Double triggerPrice = null;

  @SerializedName("order_link_id")
  private String orderLinkId = null;

  @SerializedName("created_at")
  private String createdAt = null;

  @SerializedName("updated_at")
  private String updatedAt = null;

  @SerializedName("take_profit")
  private Double takeProfit = null;

  @SerializedName("stop_loss")
  private Double stopLoss = null;

  @SerializedName("tp_trigger_by")
  private String tpTriggerBy = null;

  @SerializedName("sl_trigger_by")
  private String slTriggerBy = null;

  public LinearSearchStopOrderResult stopOrderId(String stopOrderId) {
    this.stopOrderId = stopOrderId;
    return this;
  }

   /**
   * Get stopOrderId
   * @return stopOrderId
  **/
  @ApiModelProperty(value = "")
  public String getStopOrderId() {
    return stopOrderId;
  }

  public void setStopOrderId(String stopOrderId) {
    this.stopOrderId = stopOrderId;
  }

  public LinearSearchStopOrderResult userId(Long userId) {
    this.userId = userId;
    return this;
  }

   /**
   * Get userId
   * @return userId
  **/
  @ApiModelProperty(value = "")
  public Long getUserId() {
    return userId;
  }

  public void setUserId(Long userId) {
    this.userId = userId;
  }

  public LinearSearchStopOrderResult side(String side) {
    this.side = side;
    return this;
  }

   /**
   * Get side
   * @return side
  **/
  @ApiModelProperty(value = "")
  public String getSide() {
    return side;
  }

  public void setSide(String side) {
    this.side = side;
  }

  public LinearSearchStopOrderResult symbol(String symbol) {
    this.symbol = symbol;
    return this;
  }

   /**
   * Get symbol
   * @return symbol
  **/
  @ApiModelProperty(value = "")
  public String getSymbol() {
    return symbol;
  }

  public void setSymbol(String symbol) {
    this.symbol = symbol;
  }

  public LinearSearchStopOrderResult orderType(String orderType) {
    this.orderType = orderType;
    return this;
  }

   /**
   * Get orderType
   * @return orderType
  **/
  @ApiModelProperty(value = "")
  public String getOrderType() {
    return orderType;
  }

  public void setOrderType(String orderType) {
    this.orderType = orderType;
  }

  public LinearSearchStopOrderResult price(Double price) {
    this.price = price;
    return this;
  }

   /**
   * Get price
   * @return price
  **/
  @ApiModelProperty(value = "")
  public Double getPrice() {
    return price;
  }

  public void setPrice(Double price) {
    this.price = price;
  }

  public LinearSearchStopOrderResult qty(Double qty) {
    this.qty = qty;
    return this;
  }

   /**
   * Get qty
   * @return qty
  **/
  @ApiModelProperty(value = "")
  public Double getQty() {
    return qty;
  }

  public void setQty(Double qty) {
    this.qty = qty;
  }

  public LinearSearchStopOrderResult timeInForce(String timeInForce) {
    this.timeInForce = timeInForce;
    return this;
  }

   /**
   * Get timeInForce
   * @return timeInForce
  **/
  @ApiModelProperty(value = "")
  public String getTimeInForce() {
    return timeInForce;
  }

  public void setTimeInForce(String timeInForce) {
    this.timeInForce = timeInForce;
  }

  public LinearSearchStopOrderResult orderStatus(String orderStatus) {
    this.orderStatus = orderStatus;
    return this;
  }

   /**
   * Get orderStatus
   * @return orderStatus
  **/
  @ApiModelProperty(value = "")
  public String getOrderStatus() {
    return orderStatus;
  }

  public void setOrderStatus(String orderStatus) {
    this.orderStatus = orderStatus;
  }

  public LinearSearchStopOrderResult triggerPrice(Double triggerPrice) {
    this.triggerPrice = triggerPrice;
    return this;
  }

   /**
   * Get triggerPrice
   * @return triggerPrice
  **/
  @ApiModelProperty(value = "")
  public Double getTriggerPrice() {
    return triggerPrice;
  }

  public void setTriggerPrice(Double triggerPrice) {
    this.triggerPrice = triggerPrice;
  }

  public LinearSearchStopOrderResult orderLinkId(String orderLinkId) {
    this.orderLinkId = orderLinkId;
    return this;
  }

   /**
   * Get orderLinkId
   * @return orderLinkId
  **/
  @ApiModelProperty(value = "")
  public String getOrderLinkId() {
    return orderLinkId;
  }

  public void setOrderLinkId(String orderLinkId) {
    this.orderLinkId = orderLinkId;
  }

  public LinearSearchStopOrderResult createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

   /**
   * Get createdAt
   * @return createdAt
  **/
  @ApiModelProperty(value = "")
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }

  public LinearSearchStopOrderResult updatedAt(String updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

   /**
   * Get updatedAt
   * @return updatedAt
  **/
  @ApiModelProperty(value = "")
  public String getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(String updatedAt) {
    this.updatedAt = updatedAt;
  }

  public LinearSearchStopOrderResult takeProfit(Double takeProfit) {
    this.takeProfit = takeProfit;
    return this;
  }

   /**
   * Get takeProfit
   * @return takeProfit
  **/
  @ApiModelProperty(value = "")
  public Double getTakeProfit() {
    return takeProfit;
  }

  public void setTakeProfit(Double takeProfit) {
    this.takeProfit = takeProfit;
  }

  public LinearSearchStopOrderResult stopLoss(Double stopLoss) {
    this.stopLoss = stopLoss;
    return this;
  }

   /**
   * Get stopLoss
   * @return stopLoss
  **/
  @ApiModelProperty(value = "")
  public Double getStopLoss() {
    return stopLoss;
  }

  public void setStopLoss(Double stopLoss) {
    this.stopLoss = stopLoss;
  }

  public LinearSearchStopOrderResult tpTriggerBy(String tpTriggerBy) {
    this.tpTriggerBy = tpTriggerBy;
    return this;
  }

   /**
   * Get tpTriggerBy
   * @return tpTriggerBy
  **/
  @ApiModelProperty(value = "")
  public String getTpTriggerBy() {
    return tpTriggerBy;
  }

  public void setTpTriggerBy(String tpTriggerBy) {
    this.tpTriggerBy = tpTriggerBy;
  }

  public LinearSearchStopOrderResult slTriggerBy(String slTriggerBy) {
    this.slTriggerBy = slTriggerBy;
    return this;
  }

   /**
   * Get slTriggerBy
   * @return slTriggerBy
  **/
  @ApiModelProperty(value = "")
  public String getSlTriggerBy() {
    return slTriggerBy;
  }

  public void setSlTriggerBy(String slTriggerBy) {
    this.slTriggerBy = slTriggerBy;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LinearSearchStopOrderResult linearSearchStopOrderResult = (LinearSearchStopOrderResult) o;
    return Objects.equals(this.stopOrderId, linearSearchStopOrderResult.stopOrderId) &&
        Objects.equals(this.userId, linearSearchStopOrderResult.userId) &&
        Objects.equals(this.side, linearSearchStopOrderResult.side) &&
        Objects.equals(this.symbol, linearSearchStopOrderResult.symbol) &&
        Objects.equals(this.orderType, linearSearchStopOrderResult.orderType) &&
        Objects.equals(this.price, linearSearchStopOrderResult.price) &&
        Objects.equals(this.qty, linearSearchStopOrderResult.qty) &&
        Objects.equals(this.timeInForce, linearSearchStopOrderResult.timeInForce) &&
        Objects.equals(this.orderStatus, linearSearchStopOrderResult.orderStatus) &&
        Objects.equals(this.triggerPrice, linearSearchStopOrderResult.triggerPrice) &&
        Objects.equals(this.orderLinkId, linearSearchStopOrderResult.orderLinkId) &&
        Objects.equals(this.createdAt, linearSearchStopOrderResult.createdAt) &&
        Objects.equals(this.updatedAt, linearSearchStopOrderResult.updatedAt) &&
        Objects.equals(this.takeProfit, linearSearchStopOrderResult.takeProfit) &&
        Objects.equals(this.stopLoss, linearSearchStopOrderResult.stopLoss) &&
        Objects.equals(this.tpTriggerBy, linearSearchStopOrderResult.tpTriggerBy) &&
        Objects.equals(this.slTriggerBy, linearSearchStopOrderResult.slTriggerBy);
  }

  @Override
  public int hashCode() {
    return Objects.hash(stopOrderId, userId, side, symbol, orderType, price, qty, timeInForce, orderStatus, triggerPrice, orderLinkId, createdAt, updatedAt, takeProfit, stopLoss, tpTriggerBy, slTriggerBy);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LinearSearchStopOrderResult {\n");
    
    sb.append("    stopOrderId: ").append(toIndentedString(stopOrderId)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    side: ").append(toIndentedString(side)).append("\n");
    sb.append("    symbol: ").append(toIndentedString(symbol)).append("\n");
    sb.append("    orderType: ").append(toIndentedString(orderType)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    qty: ").append(toIndentedString(qty)).append("\n");
    sb.append("    timeInForce: ").append(toIndentedString(timeInForce)).append("\n");
    sb.append("    orderStatus: ").append(toIndentedString(orderStatus)).append("\n");
    sb.append("    triggerPrice: ").append(toIndentedString(triggerPrice)).append("\n");
    sb.append("    orderLinkId: ").append(toIndentedString(orderLinkId)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    takeProfit: ").append(toIndentedString(takeProfit)).append("\n");
    sb.append("    stopLoss: ").append(toIndentedString(stopLoss)).append("\n");
    sb.append("    tpTriggerBy: ").append(toIndentedString(tpTriggerBy)).append("\n");
    sb.append("    slTriggerBy: ").append(toIndentedString(slTriggerBy)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
