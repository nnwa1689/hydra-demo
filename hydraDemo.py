from omegaconf import DictConfig, OmegaConf
import hydra
import logging

@hydra.main(config_path="config", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    print(cfg.db)
    logging.info(connecdb(cfg.db.driver, cfg.db.user, cfg.db.password))
    print(connecdb(cfg.db.driver, cfg.db.user, cfg.db.password))  

def connecdb(driver, user, password):
    return "Connected Sucsefull!! Driver:" + driver + ", user:" + user

if __name__ == "__main__":
    my_app()