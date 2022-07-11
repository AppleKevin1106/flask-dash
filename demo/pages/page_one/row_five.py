from fastapi import APIRouter
from zen_dash import instances as i


router = APIRouter(
    prefix="/backend/page_one/row_five",
    tags=["row_five"],
    responses={404: {"description": "Not found"}},
)


@router.post("/button_toggle", response_model=i.ReturnData)
async def d3():
    t =  i.ReturnData(type=i.InstanceType.BUTTON_TOGGLE,
                        title="Button Toggle",
                        button_toggle_data=i.ButtonToggleData(name="toggle_data",
                                                multiple=False,
                                                data=[i.ButtonToggleInstance(label="Red", name="red", selected=True),
                                                      i.ButtonToggleInstance(label="Blue", name="blue"),
                                                      i.ButtonToggleInstance(label="Black", name="black")]))
    return t


@router.post("/button_toggle_multiple", response_model=i.ReturnData)
async def d3():
    return i.ReturnData(type=i.InstanceType.BUTTON_TOGGLE,
                        title="Button Toggle multiple",
                        button_toggle_data=i.ButtonToggleData(name="toggle_data",
                                                multiple=True,
                                                data=[i.ButtonToggleInstance(label="Red", name="red", selected=True),
                                                      i.ButtonToggleInstance(label="Blue", name="blue"),
                                                      i.ButtonToggleInstance(label="Black", name="black")]))