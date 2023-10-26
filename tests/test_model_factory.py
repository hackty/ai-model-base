from ai_model_base.model.BaseModel import BaseModel
from ai_model_base.resource.factory.ModelFactory import ModelFactory


class FakeModel(BaseModel):

    def startup(self) -> None:
        print("fake startup")

    def shutdown(self) -> None:
        print("fake shutdown")

    def get_model_path(self) -> str:
        return "/fake/path"


def test_creation_by_mocked(mocker):
    mocked_startup = mocker.patch.object(FakeModel, 'startup')
    model = ModelFactory.create_by_class(FakeModel)
    mocked_startup.assert_called()
    assert isinstance(model, FakeModel)
    assert model.get_model_path() == "/fake/path"


def test_creation_by_spied(mocker):
    spied_startup = mocker.spy(FakeModel, 'startup')
    model = ModelFactory.create_by_class(FakeModel)
    spied_startup.assert_called()
    assert isinstance(model, FakeModel)
    assert model.get_model_path() == "/fake/path"
