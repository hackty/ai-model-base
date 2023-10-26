from ai_model_base.model.BaseModel import BaseModel
from ai_model_base.resource.pool.ModelPool import model_pool


class FakeModel(BaseModel):

    def startup(self) -> None:
        print("fake startup")

    def shutdown(self) -> None:
        print("fake shutdown")

    def get_model_path(self) -> str:
        return "/fake/path"


def test_model_lifecycle(mocker):
    mocked_startup = mocker.spy(FakeModel, 'startup')
    mocked_shutdown = mocker.spy(FakeModel, 'shutdown')
    # instantiate and initialize
    model = model_pool.get_model_by_class(FakeModel)
    mocked_startup.assert_called_once()
    assert model.get_model_name() == "FakeModel"
    assert isinstance(model, FakeModel)
    assert "FakeModel" in model_pool.list_active_model_name()
    # reuse
    anther_model = model_pool.get_model_by_class(FakeModel)
    assert anther_model == model
    mocked_startup.assert_called_once()
    # release
    model_pool.release_model_by_name("FakeModel")
    mocked_shutdown.assert_called_once()
    assert "FakeModel" not in model_pool.list_active_model_name()
