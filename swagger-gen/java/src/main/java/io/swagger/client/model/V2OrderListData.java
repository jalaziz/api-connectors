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
import io.swagger.client.model.V2OrderRes;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Get order list response
 */
@ApiModel(description = "Get order list response")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-11-12T14:39:31.513+08:00")
public class V2OrderListData {
  @SerializedName("data")
  private List<V2OrderRes> data = null;

  @SerializedName("cursor")
  private String cursor = null;

  public V2OrderListData data(List<V2OrderRes> data) {
    this.data = data;
    return this;
  }

  public V2OrderListData addDataItem(V2OrderRes dataItem) {
    if (this.data == null) {
      this.data = new ArrayList<V2OrderRes>();
    }
    this.data.add(dataItem);
    return this;
  }

   /**
   * Get data
   * @return data
  **/
  @ApiModelProperty(value = "")
  public List<V2OrderRes> getData() {
    return data;
  }

  public void setData(List<V2OrderRes> data) {
    this.data = data;
  }

  public V2OrderListData cursor(String cursor) {
    this.cursor = cursor;
    return this;
  }

   /**
   * Get cursor
   * @return cursor
  **/
  @ApiModelProperty(value = "")
  public String getCursor() {
    return cursor;
  }

  public void setCursor(String cursor) {
    this.cursor = cursor;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V2OrderListData v2OrderListData = (V2OrderListData) o;
    return Objects.equals(this.data, v2OrderListData.data) &&
        Objects.equals(this.cursor, v2OrderListData.cursor);
  }

  @Override
  public int hashCode() {
    return Objects.hash(data, cursor);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V2OrderListData {\n");
    
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    cursor: ").append(toIndentedString(cursor)).append("\n");
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
