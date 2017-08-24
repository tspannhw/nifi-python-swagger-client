# UserDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the component. | [optional] 
**parent_group_id** | **str** | The id of parent process group of this component if applicable. | [optional] 
**position** | [**PositionDTO**](PositionDTO.md) | The position of this component in the UI if applicable. | [optional] 
**identity** | **str** | The identity of the tenant. | [optional] 
**user_groups** | [**list[TenantEntity]**](TenantEntity.md) | The groups to which the user belongs. This field is read only and it provided for convenience. | [optional] 
**access_policies** | [**list[AccessPolicySummaryEntity]**](AccessPolicySummaryEntity.md) | The access policies this user belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


