import pytest

from connectkit import link


def test_link_without_a_bearer_is_an_error(monkeypatch):
    monkeypatch.delenv("PPLX_AGENT_PROXY_TOKEN", raising=False)
    monkeypatch.delenv("PPLX_CONNECTOR_API_KEY", raising=False)
    with pytest.raises(link.LinkError):
        link.link()


def test_status_is_none_when_not_linked(tmp_path, monkeypatch):
    monkeypatch.setattr(link, "STATE", tmp_path / "link.json")
    assert link.status() is None


def test_unlink_is_idempotent(tmp_path, monkeypatch):
    monkeypatch.setattr(link, "STATE", tmp_path / "link.json")
    assert link.unlink() is False
