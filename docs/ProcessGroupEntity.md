# ProcessGroupEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | [**RevisionDTO**](RevisionDTO.md) | The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses. | [optional] 
**id** | **str** | The id of the component. | [optional] 
**uri** | **str** | The URI for futures requests to the component. | [optional] 
**position** | [**PositionDTO**](PositionDTO.md) | The position of this component in the UI if applicable. | [optional] 
**permissions** | [**PermissionsDTO**](PermissionsDTO.md) | The permissions for this component. | [optional] 
**bulletins** | [**list[BulletinEntity]**](BulletinEntity.md) | The bulletins for this component. | [optional] 
**component** | [**ProcessGroupDTO**](ProcessGroupDTO.md) |  | [optional] 
**status** | [**ProcessGroupStatusDTO**](ProcessGroupStatusDTO.md) | The status of the process group. | [optional] 
**running_count** | **int** | The number of running components in this process group. | [optional] 
**stopped_count** | **int** | The number of stopped components in the process group. | [optional] 
**invalid_count** | **int** | The number of invalid components in the process group. | [optional] 
**disabled_count** | **int** | The number of disabled components in the process group. | [optional] 
**active_remote_port_count** | **int** | The number of active remote ports in the process group. | [optional] 
**inactive_remote_port_count** | **int** | The number of inactive remote ports in the process group. | [optional] 
**input_port_count** | **int** | The number of input ports in the process group. | [optional] 
**output_port_count** | **int** | The number of output ports in the process group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


